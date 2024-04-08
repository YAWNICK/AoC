import os
from collections import Counter
import functools

CARDS = 'AKQT98765432J'

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    lines = list(map(str.split, lines))
    lines = sorted(lines, key=functools.cmp_to_key(lambda x,y: cmphands(x[0], y[0])))
    l = len(lines)
    res = 0
    mj = 0
    for line in lines:
        s = line[0]
        lj = len(list(filter(lambda ch: ch == 'J', s)))
        mj = max(mj, lj)
    print('mj', mj)
    for i, item  in enumerate(lines):
        
        res += (i+1)*int(item[1])
    print(res)
    return res

def cmphands(x, y):
    rx, ry = handtype(x), handtype(y)
    if rx > ry:
        return 1
    elif ry > rx:
        return -1
    i = 0
    while x[i] == y[i]:
        i += 1
    return 1 if CARDS.index(x[i]) < CARDS.index(y[i]) else -1

def handtype(z):
    C = Counter(z)
    c = set(C.values())
    if c == {5}:
        return 7
    elif c == {4,1}:
        if 'J' in z:
            return 7
        else:
            return 6
    elif c == {3,2}:
        if 'J' in z:
            return 7
        else:
            return 5
    elif c == {3,1}:
        if 'J' in z:
            return 6
        else:
            return 4
    elif c == {2,1}:
        if len(set(z)) == 3:
            if 'J' in z:
                if C['J'] == 1:
                    return 5
                else:
                    return 6
            else:
                return 3
        else:
            if 'J' in z:
                return 4
            else:
                return 2
    else:
        if 'J' in z:
            return 2
        else:
            return 1

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [6440]
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
