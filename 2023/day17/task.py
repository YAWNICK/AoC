import os
import heapq
from collections import defaultdict

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    D = [list(map(int, line)) for line in lines]
    ylen = len(D)
    xlen = len(D[0])
    #C = [[99999]*xlen for _ in range(ylen)]
    C = [[defaultdict(lambda: 99999) for _ in range(xlen)] for _ in range(ylen)]
    # heat loss, y, x, dpy, dpx, n_straight_steps
    Q = [(0, 0, 0, 0, 0, 0)]
    while Q:
        #print(len(Q))
        hloss, y, x, dpy, dpx, steps = heapq.heappop(Q)
        #print(hloss, y, x, dpy, dpx, steps)
        if hloss >= C[y][x][(steps*dpy, steps*dpx)]:
            continue
        C[y][x][(steps*dpy, steps*dpx)] = hloss
        ####
        #for row in C:
        #    print(row)
        ####
        if y == ylen-1 and x == xlen-1:
            #print(hloss)
            break
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dy == dpy and dx == dpx:  # don't go back where I came from
                continue
            nsteps = 4
            if dy == -dpy and dx == -dpx:
                nsteps = steps + 1
            if nsteps > 10:
                continue
            dsteps = nsteps if nsteps == 4 else 1
            ny, nx = y+dsteps*dy, x+dsteps*dx
            if ny < 0 or ny >= ylen or nx < 0 or nx >= xlen:  # check bounds
                continue
            hl = D[ny][nx]
            if dsteps == 4:
                hl = sum([D[y+s*dy][x+s*dx] for s in range(1,5)])
            if hloss + hl >= C[ny][nx][(-nsteps*dpy, -nsteps*dpx)]:
                continue
            heapq.heappush(Q, (hloss+hl, ny, nx, -dy, -dx, nsteps))
            #C[ny][nx][(-dpy, -dpx)] = hloss+hl
    #print(C[ylen-1][xlen-1])
    print(hloss)
    return hloss

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [102]
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
