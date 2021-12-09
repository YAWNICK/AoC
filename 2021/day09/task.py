import os
from functools import reduce
from operator import mul

def compute(s: str, part: int):
    lines = s.splitlines()
    lines = [list(map(int, line)) for line in lines]
    lx = len(lines)  # length x
    ly = len(lines[0])  # length y
    lps = []  # low points
    res = 0  # result for part 1
    for x, line in enumerate(lines):
        for y, n in enumerate(line):
            adj = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx <= lx-1 and 0 <= ny <= ly-1:
                    adj.append(lines[nx][ny])
            if n < min(adj):
                res += n + 1
                lps.append((x, y))
    if part == 1:
        return res
    # Part 2
    bs = []  # basin sizes
    for lp in lps:
        b = set()  # basin points
        lpx, lpy = lp  # low point coordinates
        fringe = {lp}
        while len(fringe) > 0:
            b.update(fringe)
            nf = set()  # new fringe
            for x, y in fringe:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx <= lx-1 and 0 <= ny <= ly-1:
                        if lines[nx][ny] < 9 and lines[nx][ny] > lines[x][y]:
                            if (nx, ny) not in b:
                                nf.add((nx, ny))
            fringe = nf
        bs.append(len(b))
    return reduce(mul, sorted(bs)[-3:])

###############################################################################

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [1134]
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
