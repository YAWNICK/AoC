import os
from functools import cache

def compute(s: str):
    lines = s.splitlines()
    res = 0
    for line in lines:
        d, ns = line.split()
        ns = tuple(map(int, ns.split(',')))
        d = '?'.join([d]*5)
        ns = ns*5
        d += '.'
        res += count(d, ns)
    return res

@cache
def count(d, ns):
    if ns == ():
        return 0 if '#' in d else 1
    n = ns[0]
    res = 0
    max_offset = len(d)-sum(ns)-len(ns)+1
    for i in range(max_offset):
        if d[i+n] == '#':
            continue
        if '#' in d[:i]:
            break
        if '.' not in d[i:i+n]:
            res += count(d[i+n+1:], ns[1:])
    return res


def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [21]
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
