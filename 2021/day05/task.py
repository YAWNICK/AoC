import os
import re
from collections import defaultdict

def compute(s: str, part: int):
    lines = s.splitlines()
    lines = [list(map(int, re.match("(\d*),(\d*) -> (\d*),(\d*)", line).groups()))
        for line in lines]
    spots = defaultdict(int)
    for x1, y1, x2, y2 in lines:
        rx = range(x1, x2-1, -1) if x1 > x2 else range(x1, x2+1, 1)
        ry = range(y1, y2-1, -1) if y1 > y2 else range(y1, y2+1, 1)
        lrx, lry = len(rx), len(ry)
        if lrx > lry:
            ps = (rx, [y1]*lrx)
        elif lrx < lry:
            ps = ([x1]*lry, ry)
        else:
            if part == 1: continue 
            ps = (rx, ry)
        for pos in zip(*ps):
            s = f"{pos[0]},{pos[1]}"
            spots[s] += 1
    res = 0
    for cnt in spots.values():
        if cnt > 1:
            res += 1
    return res

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
