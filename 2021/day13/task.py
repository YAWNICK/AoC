import os
import numpy as np
import matplotlib.pyplot as plt

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
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
    print("Startd with", len(ps), "dots.")
    for d, val in folds:
        for x, y in ps.copy():
            if d == 'x' and x > val:
                ps.remove((x,y))
                ps.add((x - 2*(x-val), y))
            if d == 'y' and y > val:
                ps.remove((x,y))
                ps.add((x, y - 2*(y-val)))
        print(len(ps))
    l = list(ps)
    plt.scatter(*zip(*l))
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
