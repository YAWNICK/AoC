import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    ylen = len(lines)
    xlen = len(lines[0])
    maxscore = 0
    for y in range(ylen):
        s = score(lines, (y, 0, 0, -1))
        maxscore = max(maxscore, s)
        s = score(lines, (y, xlen-1, 0, 1))
        maxscore = max(maxscore, s)
    for x in range(xlen):
        s = score(lines, (0, x, -1, 0))
        maxscore = max(maxscore, s)
        s = score(lines, (ylen-1, x, 1, 0))
        maxscore = max(maxscore, s)
    print(maxscore)
    return maxscore


def score(D, start):
    ylen = len(D)
    xlen = len(D[0])
    S = [['0']*xlen for _ in range(ylen)]
    #d = (0, -1)
    #Q = [(0, 0, 0, -1)]
    Q = [start]
    while Q:
        y, x, dpy, dpx = Q.pop(0)
        if y < 0 or y >= ylen or x < 0 or x >= xlen:
            continue
        symbol = D[y][x]
        state = S[y][x]
        if symbol == '.':
            if state == '|-'[dpx] or state == '+':
                continue
            Q = [(y-dpy, x-dpx, dpy, dpx)] + Q
            S[y][x] = '+' if state in '|-' else '|-'[dpx]
            #E.add((y,x))
        elif symbol == '|':
            if state == '|':
                continue
            if dpx == 0:
                Q = [(y-dpy, x-dpx, dpy, dpx)] + Q
            else:
                Q = Q + [(y-1, x, 1, 0), (y+1, x, -1, 0)]
            S[y][x] = '|'
        elif symbol == '-':
            if state == '-':
                continue
            if dpy == 0:
                Q = [(y-dpy, x-dpx, dpy, dpx)] + Q
            else:
                Q = Q + [(y, x-1, 0, 1), (y, x+1, 0, -1)]
            S[y][x] = '-'
        elif symbol == '/':
            if state == '+':
                continue
            if (dpy == -1 or dpx == -1):
                if state == 'J':
                    continue
                else:
                    Q = [(y+dpx, x+dpy, -dpx, -dpy)] + Q
            if (dpy == 1 or dpx == 1):
                if state == 'F':
                    continue
                else:
                    Q = [(y+dpx, x+dpy, -dpx, -dpy)] + Q
            S[y][x] = '+' if state in 'JF' else '_FJ'[dpy]
        elif symbol == '\\':
            if state == '+':
                continue
            if (dpy == -1 or dpx == 1):
                if state == 'L':
                    continue
                else:
                    Q = [(y-dpx, x-dpy, dpx, dpy)] + Q
            if (dpy == 1 or dpx == -1):
                if state == '7':
                    continue
                else:
                    Q = [(y-dpx, x-dpy, dpx, dpy)] + Q
            S[y][x] = '+' if state in 'L7' else '_7L'[dpy]

    res = 0
    for i in range(ylen):
        for j in range(xlen):
            if S[i][j] != '0':
                res += 1
    #print(res)
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
