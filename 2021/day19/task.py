import os
from collections import Counter, defaultdict
import numpy as np
from copy import deepcopy
#c = list((Counter(a) & Counter(b)).elements())
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
        #print(max(cs.values()))
        m = max(cs.items(), key=lambda item: item[1])
        if m[1] >= 12:
            print(m)
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
        #print("len rest:", len(rest))
        #print("len test points:", len(test_np_points))
        ms = []
        for i, sn in enumerate(rest):
            if ps := matches(np_points, sn):
                print("MATCH!!!")
                #rest.remove(sn)
                rest.pop(i)
                ms.append(ps)
        #print("This round:", len(ms), "matches")
        for match in ms:
            points.update(match)
        print(len(points))
    print("POINTS:", len(points))
    print(coords)
    #for i, sn in enumerate(ss):
    #    for j, sm in enumerate(ss[i+1:])
    #        if ps := matches(s0, sn):
    #            print(i, 'matches!!!')
    #            points.update(ps)
    #            print(len(points))
    return 

def compute2():
    cs = [[    4,    47, -1267], [-1258,    49, -1267], [ 1074,    32, -1341], [ 1110,    51, -2440], [ 2258,    18, -1189], [ 3450,    70, -1337], [ 2398,   -33, -2485], [ 1027, -1288, -1269], [ 3535,    58, -2506], [ 2306,   -92, -3602], [ 3450, -1269, -1281], [ 3466,  1266, -1242], [ 1201, -1241,     8], [ 1089, -2498,  -141], [ 2277,  1100, -3708], [ 4808, -1260, -1223], [ 3614,   -37, -3709], [ 3614, -1233,   -84], [ 2295, -2518, -1152], [ 2379, -1273, -3685], [ 2348, -1129, -4890], [ 4650,   -71, -3704], [ 2233, -2346, -3656], [ 1045, -1158, -3701], [ 3591, -1195, -3613], [ 3521,    45, -4834], [ 4639,   -28, -1265], [ 2284, -3607, -1157], [ 3601, -2448, -1175], [ 5892,    -6, -1222], [ 2416, -1143, -5988], [ 1152, -2397, -4904], [ 1064, -2455, -3581], [ 5965,    49, -2516], [ 2359, -2524, -2370], [ 2414, -2378, -4758], [  -16, -2343,   -81]]
    cs.append([0,0,0])
    m = 0
    for a in cs:
        for b in cs:
            md = sum(np.array(a)-np.array(b))
            m = max(m, md)
    print(m)
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
    print(compute2())

if __name__ == "__main__":
    main()
