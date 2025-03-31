import os
from tqdm import tqdm

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    n = len(lines)
    D = []
    s = None
    for y in range(n):
        for x in range(n):
            if lines[y][x] == '#':
                D.append((y,x))
            elif lines[y][x] == '^':
                s = (y,x)
    for i in range(-1, n+1):
        D.append((-1, i))
        D.append((i, -1))
        D.append((n, i))
        D.append((i, n))
    yy = set([y for y,x in D])
    xx = set([x for y,x in D])
    res = 0
    for y in tqdm(yy):
        for x in xx:
            DD = D.copy()
            DD.append((y,x))
            if calc(DD, s, n):
                res += 1
    
    print(res)

    return res

def calc(D, s, n):
    pos = s
    heading = (-1,0)
    P = {(s[0], s[1], heading[0], heading[1])} 
    HEADINGS = [(-1,0),(0,1),(1,0),(0,-1)]
    while d := find_d(pos[0],pos[1],heading,D):
        for i in range(max(abs(pos[0]-d[0]), abs(pos[1]-d[1]))-1):
            np = (pos[0]+(i+1)*heading[0], pos[1]+(i+1)*heading[1], heading[0], heading[1])
            if np in P:
                return True
            P.add(np)
        if -1 in d or n in d:
            break
        pos = (d[0]+-1*heading[0], d[1]+-1*heading[1])
        heading = HEADINGS[(HEADINGS.index(heading)+1) % 4]
    #return len(P)
    return False

def find_d(py, px, heading, D):
    d = None
    if heading[0] == 0:
        ds = set(filter(lambda d: d[0] == py, D))
        if heading[1] == 1:
            cands = list(filter(lambda e: e[1] > px, ds))
            if not cands:
                return None
            d = min(cands, key=lambda e: e[1])

        else:
            cands = list(filter(lambda e: e[1] < px, ds))
            if not cands:
                return None
            d = max(cands, key=lambda e: e[1])
    else:
        ds = set(filter(lambda d: d[1] == px, D))
        if heading[0] == 1:
            cands = list(filter(lambda e: e[0] > py, ds))
            if not cands:
                return None
            d = min(cands, key=lambda e: e[0])
        else:
            cands = list(filter(lambda e: e[0] < py, ds))
            if not cands:
                return None
            d = max(cands, key=lambda e: e[0])
    return d


def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [41]
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
