import os
import numpy as np
import matplotlib.pyplot as plt

def compute(s: str):
    lines = s.splitlines()
    ps = set()
    folds = []
    ip = 0
    for line in lines:
        if line == '':
            ip = 1
            continue
        if ip == 0:
            x, y = line.split(',')
            ps.add((int(x),int(y)))
        else:
            d, val = line.split('=')
            folds.append((d[-1], int(val)))
    #print("Startd with", len(ps), "dots.")
    for i, (d, val) in enumerate(folds):
        for x, y in ps.copy():
            if d == 'x' and x > val:
                ps.remove((x,y))
                ps.add((x - 2*(x-val), y))
            if d == 'y' and y > val:
                ps.remove((x,y))
                ps.add((x, y - 2*(y-val)))
        if i == 0:
            print("Part 1:", len(ps))
    l = list(ps)
    ml = max(map(lambda x: x[1], l))
    l = list(map(lambda x: (x[0], ml-x[1]), l))
    print("Part 2: see plot.")
    plt.scatter(*zip(*l))
    plt.subplots_adjust(bottom=0.73)
    plt.show()
    return 

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
