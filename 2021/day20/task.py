import os
from collections import defaultdict

def compute(s: str, part: int):
    lines = s.splitlines()
    lookup, lines = lines[0], lines[2:]
    ps = defaultdict(int)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                ps[(i,j)] = 1
    xmin, xmax, ymin, ymax = 0, len(lines)-1, 0, len(lines[0])-1
    N = 2 if part == 1 else 50
    for steps in range(N):
        newps = defaultdict(int) if steps % 2 == 1 else defaultdict(lambda: 1)
        for i in range(xmin-1, xmax+2):
            for j in range(ymin-1, ymax+2):
                ns = ''
                for di, dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)):
                    ns += str(ps[(i+di,j+dj)])
                symbol = lookup[int(ns, 2)]
                if steps % 2 == 0:
                    if symbol == '.':
                        newps[(i,j)] = 0
                else:
                    if symbol == '#':
                        newps[(i,j)] = 1
        ps = newps
        xmin -= 1
        xmax += 1
        ymin -= 1
        ymax += 1
    return list(ps.values()).count(1)

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [35]
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
    print("Part 1:", compute(inp, 1))
    print("Part 2:", compute(inp, 2))

if __name__ == "__main__":
    main()
