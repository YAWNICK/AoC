import os
from functools import reduce
import numpy as np


def compute1(s: str):
    lines = s.splitlines()
    rlen = len(lines[0])
    lines = list(map(lambda s: np.array(list(map(int, s))), lines))
    lines = list(map(lambda xs: np.where(xs==0, -1, xs), lines))
    bits1 = [condition(lines, i, True) for i in range(rlen)]
    bits2 = [condition(lines, i, False) for i in range(rlen)]
    return int(''.join(map(str, bits1)), 2)*int(''.join(map(str, bits2)), 2)

def compute2(s: str):
    lines = s.splitlines()
    rlen = len(lines[0])
    lines_o = list(map(lambda s: np.array(list(map(int, s))), lines))
    lines = list(map(lambda xs: np.where(xs==0, -1, xs), lines_o))
    res1 = findmeasure(lines, True)
    res2 = findmeasure(lines, False)
    return res1*res2

def findmeasure(data, most):
    keep = set(range(len(data)))
    bit = 0
    while len(keep) > 1:
        rows = [data[i] for i in keep]
        c = condition(rows, bit, most)
        c = -1 if c == 0 else c
        for i, row in enumerate(data):
            if row[bit] != c and i in keep:
                keep.remove(i)
        bit += 1
    r = data[keep.pop()]
    r = np.where(r == -1, 0, r)
    return int(''.join(map(str, r)), 2)


def condition(data, i, most):
    s = sum([xs[i] for xs in data])
    if most is True:
        return int(s >= 0)
    else:
        return int(s < 0)

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
        if compute2(read_input(f"tests/{cnt}.txt")) == solutions[cnt - 1]:
            print(f"Test {cnt} successful!")
        else:
            print(f"Test {cnt} failed!")
            print(f"  was supposed to be {solutions[cnt - 1]}")
        cnt += 1
    print("---TESTS END---")

def main():
    run_tests()
    inp = read_input("input.txt")
    print("Part 1:", compute1(inp))
    print("Part 2:", compute2(inp))

if __name__ == "__main__":
    main()
