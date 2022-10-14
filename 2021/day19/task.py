import os
from collections import Counter, defaultdict
import numpy as np
from copy import deepcopy
coords = []

def roll(p):
    return np.array([p[0], p[2], -p[1]])

def turn(p):
    return np.array([-p[1], p[0], p[2]])

def ori(p):
    r = []
    for i in range(2):
        for j in range(3):
            p = roll(p)
            r.append(p)
            for k in range(3):
                p = turn(p)
                r.append(p)
        p = roll(turn(roll(p)))
    return r

def orientations(s):
    r = list(zip(*map(ori, s)))
    return r

def matches(s1, s2):
    global coords
    sos = orientations(s2)
    assert len(sos) == 24
    for so in sos:
        cs = defaultdict(int)
        for p1 in s1:
            for p2 in so:
                cs[tuple(p1-p2)] += 1
        m = max(cs.items(), key=lambda item: item[1])
        if m[1] >= 12:
            pos = np.array(m[0])
            coords.append(pos)
            ps = set(map(lambda p: tuple(pos+p), so))
            return ps
    return set()

def compute(s: str):
    global coords
    lines = s.splitlines()
    ss = []
    s = []
    for line in lines:
        if line.startswith('---'):
            continue
        if line == '':
            ss.append(s)
            s = []
            continue
        s.append(np.array(list(map(int, line.split(',')))))
    if s:
        ss.append(s)
    ### Parsing over
    s0 = ss[0]
    points = set(map(tuple, s0))
    rest = ss[1:]
    while rest:
        np_points = list(map(np.array, points))
        ms = []
        for i, sn in enumerate(rest):
            if ps := matches(np_points, sn):
                rest.pop(i)
                ms.append(ps)
        for match in ms:
            points.update(match)
    print("Part 1:", len(points))
    coords.append(np.array([0,0,0]))
    m = 0
    for a in coords:
        for b in coords:
            md = sum(map(abs, a-b))
            m = max(m, md)
    print("Part 2:", m)
    return 

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [1]
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
    compute(inp)

if __name__ == "__main__":
    main()
