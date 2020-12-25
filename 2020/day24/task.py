import os
import re

pfromd = {'sw':[0,-1],'w':[-1,0],'nw':[-1,1],'ne':[0,1],'e':[1, 0],'se':[1,-1]}

class Node:

    def __init__(self):
        self.se = None
        self.sw = None
        self.ne = None
        self.nw = None
        self.e = None
        self.w = None

def opp(d):
    ds = ['se', 'sw', 'w', 'nw', 'ne', 'e']
    return ds[(ds.index(d)+3)%6]

def updatepos(pos, d):
    p = pfromd[d]
    pos[0] += p[0]
    pos[1] += p[1]
    return pos

def addfromcenter(dirs, center, allns):
    curr = center
    pos = [0,0]
    for d in dirs:
        pos = updatepos(pos, d)
        if getattr(curr, d) == None:
            new = Node()
            for dd in pfromd.keys():
                p = pfromd[dd]
                cpos = (pos[0] + p[0], pos[1] + p[1])
                if cpos in allns.keys():
                    setattr(new, dd, allns[cpos])
                    setattr(allns[cpos], opp(dd), new)
            allns[tuple(pos)] = new
        else:
            curr = getattr(curr, d)
    return pos

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    nl = []
    center = Node()#[0,0])
    allns = {(0,0): center}
    for line in lines:
        l = re.findall("se|sw|ne|nw|e|w", line)
        pos = addfromcenter(l, center, allns)
        if pos in nl:
            nl.remove(pos)
        else:
            nl.append(pos)
    print("Part 1:", len(nl))
    nl = list(map(tuple, nl))
    for i in range(100):
        #print("STEP", i+1)
        nalive = {}
        for pos in nl:
            for d in pfromd.values():
                npos = (pos[0]+d[0], pos[1]+d[1])
                nalive.setdefault(npos, 0)
                nalive[npos] += 1
        nnl = []
        for p, cnt in nalive.items():
            if (p in nl) and cnt == 1 or cnt == 2:
                nnl.append(p)
        nl = nnl
    return len(nl)

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [2208]
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
    #run_tests()
    inp = read_input("input.txt")
    print("Part 2", compute(inp))

if __name__ == "__main__":
    main()
