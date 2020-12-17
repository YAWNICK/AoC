import os
from copy import deepcopy

# solution only for part two
# it's slow and stores a lot of unnecessary information

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    td = [[lines]]
    td = enlarge(td)
    for i in range(6):
        td = enlarge(td)
        td = step(td)
    total2 = 0
    for w in td:
        for i in w:
            for j in i:
                total2 += j.count('#')
    return total2

def enlarge(td):
    d = len(td[0][0][0])
    d4 = len(td[0])
    for w in td:
        for i, y in enumerate(w):
            yc = y.copy()
            for j, z in enumerate(yc):
                yc[j] = '.' + z + '.'
            yc.insert(0, '.'*(d+2))
            yc.append('.'*(d+2))
            w[i] = yc
        w.insert(0, ['.'*(d+2)]*(d+2))
        w.append(['.'*(d+2)]*(d+2))
    td.insert(0, [['.'*(d+2)]*(d+2)]*(d4+2))
    td.append([['.'*(d+2)]*(d+2)]*(d4+2))
    return td

def step(td):
    new = deepcopy(td)
    for h, w in enumerate(td[1:-1]):
        for i, y in enumerate(w[1:-1]):
            for j, z in enumerate(y[1:-1]):
                for k, x in enumerate(z[1:-1]):
                    rh = h + 1
                    ri = i + 1
                    rj = j + 1
                    rk = k + 1
                    sa = 0
                    for dw in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                for dz in [-1, 0, 1]:
                                    if dw == dx == dy == dz == 0:
                                        continue
                                    if td[h+1+dw][i+1+dx][j+1+dy][k+1+dz] == '#':
                                        sa += 1
                    if sa not in [2, 3] and x == '#':
                        new[rh][ri][rj] = new[rh][ri][rj][:rk] + '.' + new[rh][ri][rj][rk+1:]
                    elif sa == 3 and x == '.':
                        new[rh][ri][rj] = new[rh][ri][rj][:rk] + '#' + new[rh][ri][rj][rk+1:]
    return new


def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [848]
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
