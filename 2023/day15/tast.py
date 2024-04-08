import os
from collections import defaultdict

def compute(s: str):
    ## if single value:
    s = s.strip()
    ## if multiple values in multiple lines
    #lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    seq = s.split(',')
    H = defaultdict(list)
    for cmd in seq:
        if '=' in cmd:
            label, fl = cmd.split('=')
            box = hash(label)
            blen = len(H[box])
            replaced = False
            for i in range(blen):
                if H[box][i][0] == label:
                    H[box][i] = (label, fl)
                    replaced = True
                    break
            if not replaced:
                H[box].append((label, fl))
        else:
            label = cmd[:-1]
            box = hash(label)
            popind = None
            for i in range(len(H[box])):
                if H[box][i][0] == label:
                    popind = i
                    break
            if popind is not None:
                H[box].pop(popind)
    res = 0
    for i in range(256):
        for j in range(len(H[i])):
            res += (i+1)*(j+1)*int(H[i][j][1])
    #return sum(map(hash, seq))
    return res

def hash(s):
    curr = 0
    for ch in s:
        curr += ord(ch)
        curr *= 17
        curr = curr % 256
    return curr

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
