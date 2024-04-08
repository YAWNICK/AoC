import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    ylen = len(lines)
    xlen = len(lines[0])
    gs = []
    for y in range(ylen):
        for x in range(xlen):
            if lines[y][x] == '#':
                gs.append([y,x])
    mtrows = []
    for y in range(ylen):
        if '#' not in lines[y]:
            mtrows.append(y)
    mtcols = []
    lines = list(zip(*lines))
    for x in range(xlen):
        if '#' not in lines[x]:
            mtcols.append(x)
    for y in mtrows[::-1]:
        for g in gs:
            if g[0] > y:
                g[0] += 999999
    for x in mtcols[::-1]:
        for g in gs:
            if g[1] > x:
                g[1] += 999999
    lg = len(gs)
    res = 0
    for i in range(lg):
        for j in range(i):
            res += abs(gs[i][0]-gs[j][0])+abs(gs[i][1]-gs[j][1])
    return res

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
