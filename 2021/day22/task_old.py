import os
from collections import defaultdict
from functools import reduce
from operator import mul
import re

class Block:

    def __init__(self,on,xmin,xmax,ymin,ymax,zmin,zmax):
        self.on = on
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax
        self.children = []
        self.children_created = False
        self.vol = (xmax-xmin+1)*(ymax-ymin+1)*(zmax-zmin+1)
        self.vol_wc = None
    
    def __str__(self):
        return str((self.xmin,self.xmax,self.ymin,self.ymax,self.zmin,self.zmax))

    def get_coords(self):
        return (self.xmin,self.xmax,self.ymin,self.ymax,self.zmin,self.zmax)

    def get_children(self, max_depth):
        self._get_children(0, max_depth)

    def _get_children(self, depth, max_depth):
        print(" "*depth, self)
        if depth == max_depth:
            return
        for c in self.children:
            c._get_children(depth+1, max_depth)
    
    def num_children(self):
        n = len(self.children)
        for c in self.children:
            n += c.num_children()
        return n

    def update_status(self, on):
        self.on = on
        for child in self.children:
            child.update_status(on)

    # should be calles once the entire tree structure is created
    def setup_volumes_wc(self):
        print("begin calculation")
        if self.vol_wc is not None:
            return self.vol_wc
        if not self.children:
            print("end", self.vol)
            self.vol_wc = self.vol
            return self.vol_wc
        #self.vol_wc = self.vol-sum([c.setup_volumes_wc() for c in self.children])
        vol_wc = self.vol
        print("start value", vol_wc)
        q = set(self.children)
        while q:
            nq = set()
            for b in q:
                bvol_wc = b.setup_volumes_wc()
                nq.update(b.children)
                vol_wc -= bvol_wc
                print("subtract child", bvol_wc)
            q = nq
        self.vol_wc = vol_wc
        print("final vol_wc is", vol_wc)
        return self.vol_wc

    def check_volumes(self):
        if not self.children:
            return self.vol
        vol = self.vol_wc
        for child in self.children:
            vol += child.check_volumes()
        return vol

    def on_cnt(self):
        return self._on_cnt_rec(set())

    def _on_cnt_rec(self, seen):
        seen.add(self)
        vol = self.vol_wc if self.on else 0
        if not self.children:
            #print("endrec returning vol", vol)
            return vol
        for child in self.children:
            if child not in seen:
                vol += child._on_cnt_rec(seen)
        #print("returning vol", vol)
        return vol

    # only call this on root blocks
    # return delta of points
    def apply(self, state):
        on_cnt = self.on_cnt()
        print("on_cnt", on_cnt)
        self.update_status(state)
        if state:
            return self.vol - on_cnt
        else:
            return -1 * on_cnt


boxes = dict()

def isin(l,xmin,xmax,ymin,ymax,zmin,zmax,x,y,z):
    return xmin <= x <= xmax and ymin <= y <= ymax and zmin <= z <= zmax

def corners(l,xmin,xmax,ymin,ymax,zmin,zmax):
    return [(x,y,z) for x in (xmin,xmax) for y in (ymin,ymax) for z in
            (zmin,zmax)]

def intersect(b1, b2):
    if b1.xmax < b2.xmin or b2.xmax < b1.xmin or b1.ymax < b2.ymin or b2.ymax < b1.ymin or b1.zmax < b2.zmin or b2.zmax < b1.zmin:
        return ()
    xmin = max(b1.xmin, b2.xmin)
    xmax = min(b1.xmax, b2.xmax)
    ymin = max(b1.ymin, b2.ymin)
    ymax = min(b1.ymax, b2.ymax)
    zmin = max(b1.zmin, b2.zmin)
    zmax = min(b1.zmax, b2.zmax)
    return (xmin,xmax,ymin,ymax,zmin,zmax)


def create_subblocks(bs):
    global boxes
    #print(list(map(str,bs)))
    #sbs = {b:[] for b in bs}
    bs = list(filter(lambda b: not b.children_created, bs))
    for i, b1 in enumerate(bs):
        for j, b2 in enumerate(bs[i+1:]):
            if b := intersect(b1, b2):
                #if b1 == bs[0]:
                    #print(b)
                if b in boxes:
                    block = boxes[b]
                else:
                    block = Block(False, *b)
                    boxes[b] = block
                b1.children.append(block)
                b2.children.append(block)
                #sbs[b1].append(block)
    for k, b in enumerate(bs):
        #if k == 0:
        #    print(b)
        #    print("children:", len(b.children))
        #    print(list(map(str,b.children)))
        create_subblocks(b.children)
        b.children_created = True


def compute(s: str):
    lines = s.splitlines()
    pat = '(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'
    lines = [(l,int(xmin),int(xmax),int(ymin),int(ymax),int(zmin),int(zmax)) for l,xmin,xmax,ymin,ymax,zmin,zmax in map(lambda line: re.match(pat, line).groups(), lines)]
    print(len(lines))
    cubes, q = [], []
    states = []
    for i, cube in enumerate(lines[:20]):
        block = Block(False, *(cube[1:]))
        cubes.append(block)
        q.append(block)
        states.append(True if cube[0] == 'on' else False)
    print("root blocks created")
    ints = 0
    create_subblocks(q)
    print(cubes[0].num_children())

    #print("setup block volumes")
    #for block in cubes[:1]:
    #    block.setup_volumes_wc()
    '''
    for block in cubes:
        if block.check_volumes() != block.vol:
            print("ERROR")
            print("ist:", block.check_volumes())
            print("soll:", block.vol)
    # actual operation
    print("begin operation")
    ps = 0
    for i, block in enumerate(cubes[:20]):
        print("apply cuboid", i, states[i])
        ps += block.apply(states[i])
        print("ps:", ps)
    
    #print(res)
    print(ps)
    '''
    return 

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = []
    # testing begins here
    cnt = 1
    while os.path.exists(f"tests/{cnt}.txt"):
        if compute(read_input(f"tests/{cnt}.txt")) == solutions[cnt - 1]:
            print(f"Test {cnt} successful!")
        else:
            print(f"Test {cnt} failed!")
            print(f"  was supposed to be {solutions[cnt - 1]}")
        cnt += 1
    print("---TESTS END---")

def main():
    run_tests()
    inp = read_input("input.txt")
    print(compute(inp))

if __name__ == "__main__":
    main()
