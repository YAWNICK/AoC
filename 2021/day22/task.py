import os
from collections import defaultdict
from functools import reduce
from operator import mul
import re

class Block:

    def __init__(self,on,xmin,xmax,ymin,ymax,zmin,zmax):
        if type(on) == str:
            self.on = True if on == 'on' else False
        else:
            self.on = on
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax
        self.vol = (xmax-xmin+1)*(ymax-ymin+1)*(zmax-zmin+1)
    
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

def points_lit(bs):
    if not bs:
        return 0
    if len(bs) == 1:
        b = bs[0]
        return b.vol if b.on else 0
    prev, b = bs[:-1], bs[-1]
    total_before_latest = points_lit(bs[:-1])
    ints = []
    for pb in prev:
        intersection = intersect(b, pb)
        if not intersection:
            continue
        ints.append(Block(pb.on, *(intersect(b, pb))))
    on_cnt_in_b = points_lit(ints)
    if b.on:
        return total_before_latest + (b.vol - on_cnt_in_b)
    else:
        return total_before_latest - on_cnt_in_b


def compute(s: str, part: int):
    lines = s.splitlines()
    pat = '(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'
    lines = [(l,int(xmin),int(xmax),int(ymin),int(ymax),int(zmin),int(zmax)) for l,xmin,xmax,ymin,ymax,zmin,zmax in map(lambda line: re.match(pat, line).groups(), lines)]
    cubes = []
    if part == 1:
        lines = lines[:20]
    for i, cube in enumerate(lines):
        block = Block(*cube)
        cubes.append(block)
    return points_lit(cubes) 

###############################################################################

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
    print("Part 1:", compute(inp, 1))
    print("Part 2:", compute(inp, 2))

if __name__ == "__main__":
    main()
