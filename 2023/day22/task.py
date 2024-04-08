import os
from pprint import pprint
from collections import defaultdict
from copy import deepcopy

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    P = []
    for line in lines:
        x, y = line.split('~')
        x1, y1, z1 = map(int, x.split(','))
        x2, y2, z2 = map(int, y.split(','))
        P.append((min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2), min(z1, z2), max(z1, z2)))
    P.sort(key=lambda x: x[4])
    plen = len(P)
    PI = {p: i for i, p in enumerate(P)}
    R = []  # sorted list of index_in_P, height pairs
    Gup = defaultdict(set)
    Gdown = defaultdict(set)
    H = [[(0, None)]*10 for _ in range(10)]
    for i, (x1, x2, y1, y2, z1, z2) in enumerate(P):
        hs = []
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                hs.append(H[x][y])
        h = max(map(lambda x: x[0],hs))
        assert h <= z1
        hnew = h+(1+(z2-z1))
        R.append((i, hnew))
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                H[x][y] = (hnew, i)
        for piece in map(lambda x: x[1], filter(lambda p: p[0] == h, hs)):
            if piece is None:
                continue
            Gup[piece].add(i)
            Gdown[i].add(piece)
        #print('--------')
        #print('piece:', x1,x2,y1,y2,z1,z2)
        #for row in H:
        #    print(row)
        #pprint(Gup)
        #pprint(Gdown)
    #print(Gup)
    #print(Gdown)
    R.sort(key=lambda x: x[1])

    dis = []
    for i in range(plen):
        disintegrated = True
        for pup in Gup[i]:
            if len(Gdown[pup]) == 1:
                disintegrated = False
        if disintegrated:
            dis.append(i)
            #print(i, P[i])
    
    for i, h in R:
        if h == 1:
            print(i, 'lies on the floor')
    floor = 13
    ress = []
    for i, _ in R[::-1]:
        Hdown = deepcopy(Gdown)
        Q = [i]
        while Q:
            piece = Q.pop(0)
            for nb in Gup[piece]:
                Hdown[nb].remove(piece)
                if Hdown[nb] == set():
                    Q.append(nb)
        cnt = 0
        for p, down in Hdown.items():
            if down == set():
                cnt += 1
        print('num pieces that fall', cnt)
        ress.append(cnt)

    res = sum(ress)
    print(res)
    return res

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [5]
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
