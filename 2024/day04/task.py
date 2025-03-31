import os
from collections import defaultdict, Counter
from parsing import parse

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    x_len = len(lines[0])
    y_len = len(lines)
    res = 0
    for y in range(y_len):
        for x in range(x_len):
            if lines[y][x] != 'X':
                continue
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                found = True
                for i, c in enumerate('MAS'):
                    nx, ny = x+(i+1)*dx, y+(i+1)*dy
                    if nx < 0 or nx >= x_len or ny < 0 or ny >= y_len:
                        found = False
                        break
                    if lines[ny][nx] != c:
                        found = False
                        break
                if found:
                    res += 1
    return res

def compute2(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    xlen = len(lines[0])
    ylen = len(lines)
    print(xlen, ylen)
    res = 0
    #d0 = lines
    #d1 = lines[::-1]
    #d2 = [line[::-1] for line in d0]
    #d3 = [line[::-1] for line in d1]
    d = lines
    #for d, xlen, ylen in [(d0,xlen,ylen), (d1,xlen,ylen), (d2,ylen,xlen), (d3,ylen,xlen)]:
    for y in range(ylen-2):
        for x in range(xlen-2):
            if d[y][x] == 'M' and d[y+2][x] == 'M' and d[y+1][x+1] == 'A' and d[y][x+2] == 'S' and d[y+2][x+2] == 'S':
                res += 1
                continue
            if d[y][x] == 'M' and d[y+2][x] == 'S' and d[y+1][x+1] == 'A' and d[y][x+2] == 'M' and d[y+2][x+2] == 'S':
                res += 1
                continue
            if d[y][x] == 'S' and d[y+2][x] == 'M' and d[y+1][x+1] == 'A' and d[y][x+2] == 'S' and d[y+2][x+2] == 'M':
                res += 1
                continue
            if d[y][x] == 'S' and d[y+2][x] == 'S' and d[y+1][x+1] == 'A' and d[y][x+2] == 'M' and d[y+2][x+2] == 'M':
                res += 1
                continue
            
            #print(y, x)
    print(res)
    return res

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [9]
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
    print(compute2(inp))

if __name__ == "__main__":
    main()
