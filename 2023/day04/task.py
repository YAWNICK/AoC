import os
from collections import defaultdict

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    G = defaultdict(int)
    lmax = len(lines)+1
    res = 0
    for i in range(lmax-1):
        G[i+1] = 1
    for line in lines:
        card, line = line.split(': ')
        cid = int(card[5:])
        w = set(map(int, line.split(' | ')[0].split()))
        m = set(map(int, line.split(' | ')[1].split()))
        s = len(w.intersection(m))
        if s > 0:
            res += 2**(s-1)
        for i in range(s):
            if cid+s+1 > lmax:
                continue
            G[cid+i+1] += G[cid]
    p2 =  sum(G.values())
    return p2

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [13]
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
