import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    d = [list(line) for line in lines]
    s = score(d)
    scores = [s]
    for _ in range(1078):
        d = shift(d, 'n')
        d = shift(d, 'w')
        d = shift(d, 's')
        d = shift(d, 'e')
        ns = score(d)
        i = None
        if ns in scores:
            i = scores[::-1].index(ns)
        print(ns, i)
        scores.append(ns)
    for line in d:
        print(''.join(line))
    res = score(d)
    print(res)
    return res

def score(d):
    score = 0
    ylen = len(d)
    xlen = len(d[0])
    for i in range(ylen):
        for j in range(xlen):
            if d[i][j] == 'O':
                score += ylen - i
    return score

def shift(d, side):
    if side == 'w':
        d = list(map(list, zip(*d)))
        d = shiftUp(d)
        d = list(map(list, zip(*d)))
    elif side == 's':
        d = d[::-1]
        d = shiftUp(d)
        d = d[::-1]
    elif side == 'e':
        d = list(map(list, zip(*d)))[::-1]
        d = shiftUp(d)
        d = list(map(list, zip(*d[::-1])))
    elif side == 'n':
        d = shiftUp(d)
    return d

def shiftUp(d):
    ylen = len(d)
    xlen = len(d[0])
    for i in range(1, ylen):
        for j in range(xlen):
            if d[i][j] == 'O':
                inew = find_shiftup_index(d, i, j)
                d[i][j] = '.'
                d[inew][j] = 'O'
    return d

def find_shiftup_index(d, i, j):
    inew = i
    while inew > 0:
        if d[inew-1][j] != '.':
            break
        inew -= 1
    return inew

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [64]
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
    print(compute(inp))

if __name__ == "__main__":
    main()
