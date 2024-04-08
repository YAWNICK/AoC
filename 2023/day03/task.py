import os
from collections import defaultdict

digits = list(map(str, range(10)))

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    res = 0
    ymax = len(lines)-1
    xmax = len(lines[0])-1
    G = defaultdict(list)
    for y in range(len(lines)):
        line = lines[y]
        x = 0
        while x <= xmax:
            ch = line[x]
            if ch not in digits:
                x += 1
                continue
            ch1 = line[x+1] if x <= xmax-1 and line[x+1] in digits else None
            ch2 = line[x+2] if x <= xmax-2 and line[x+2] in digits else None
            ps = [(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
            partial = check(lines, x, y, xmax, ymax, ps)
            if ch1 is None:
                if not partial:
                    partial = check(lines, x, y, xmax, ymax, [(1,0)])
                n = int(ch)
                #res += int(ch) if partial else 0
                newx = x + 1
            elif ch2 is None:
                if not partial:
                    partial = check(lines, x, y, xmax, ymax, [(2,-1),(2,0),(2,1)])
                n = int(ch+ch1)
                #res += int(ch+ch1) if partial else 0
                newx = x + 2
            else:
                if not partial:
                    partial = check(lines, x, y, xmax, ymax, [(2,-1),(3,-1),(3,0),(3,1),(2,1)])
                n = int(ch+ch1+ch2)
                #res += int(ch+ch1+ch2) if partial else 0
                newx = x + 3
            if partial:
                res += n
                G[partial].append(n)
            
            x = newx
    p2 = 0
    for ns in G.values():
        if len(ns) == 2:
            p2 += ns[0]*ns[1]
    return p2

def check(lines, x, y, xmax, ymax, ps):
    for i, j in ps:
        if 0 <= x+i <= xmax and 0 <= y+j <= ymax:
            #if lines[y+j][x+i] not in digits+['.']:
            if lines[y+j][x+i] == '*':
                return (y+j, x+i)
    return False

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
