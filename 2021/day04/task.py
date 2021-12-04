import os
import numpy as np

def compute1(s: str):
    lines = s.splitlines()
    xs, lines = lines[0], lines[2:]
    xs = list(map(int, xs.split(',')))
    bs = [[list(map(int, row.split())) for row in lines[i:i+5]] for i in range(0, len(lines), 6)]
    for x in xs:
        for b in bs:
            res, n = markxonb(b, x)
            if res:
                return n

def compute2(s: str):
    lines = s.splitlines()
    xs, lines = lines[0], lines[2:]
    xs = list(map(int, xs.split(',')))
    bs = [[list(map(int, row.split())) for row in lines[i:i+5]] for i in range(0, len(lines), 6)]
    wins = set(range(len(bs)))
    for x in xs:
        for i, b in enumerate(bs):
            res, n = markxonb(b, x)
            if res and i in wins:
                wins.remove(i)
            if len(wins) == 0:
                return n

def markxonb(b, x):
    for r, row in enumerate(b):
        for i, elem in enumerate(row):
            if x == elem:
                row[i] *= -1
                res, n = checkwin(b, r, i)
                if res:
                    return True, n
                else:
                    return False, 0
    return False, 0

def checkwin(b, r, i):
    if abs(sum(map(np.sign, b[r]))) == 5 or abs(sum(map(np.sign, [rr[i] for rr in b]))) == 5:
        n = b[r][i]
        ns = filter(lambda x: x >= 0, sum(b, []))
        return True, sum(ns) * n * -1
    return False, 0


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
    print("Part 1:", compute1(inp))
    print("Part 2:", compute2(inp))

if __name__ == "__main__":
    main()
