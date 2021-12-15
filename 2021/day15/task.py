import os
from copy import deepcopy


def prep(lines):
    for line in lines:
        original = line.copy()
        for i in range(4):
            line += list(map(lambda x: x+i+1 if x+i+1 < 10 else x+i+1-9, original))
    original = deepcopy(lines)
    for i in range(4):
        lines += [list(map(lambda x: x+i+1 if x+i+1 < 10 else x+i+1-9, line)) for line in original]
    return lines


def compute(s: str):
    lines = s.splitlines()
    lines = [list(map(int, line)) for line in lines]
    lines = prep(lines)
    lx = len(lines[0])
    ly = len(lines)
    costs = {}
    fringe = {(1,0): (6, lx-1-1+ly-1), (0,1): (2, lx-1+ly-1-1)}
    while True:
        node = sorted(fringe.items(), key=lambda x: sum(x[1]))[0]
        x, y, cost, md = node[0][0], node[0][1], node[1][0], node[1][1]
        fringe.pop((x,y))
        if (x,y) in costs:
            if cost < costs[x,y]:
                costs[(x,y)] = cost
        else:
            costs[(x,y)] = cost
        if md == 0:
            return cost
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx <= lx-1 and 0 <= ny <= ly-1:
                ncost = cost + lines[nx][ny]
                nmd = lx-1-nx+ly-1-ny
                if (nx, ny) in fringe:
                    if ncost + nmd < sum(fringe[(nx, ny)]):
                        fringe[(nx, ny)] = (ncost, nmd)
                else:
                    if (nx, ny) in costs:
                        if ncost < costs[(nx, ny)]:
                            fringe[(nx, ny)] = (ncost, nmd)
                    else:
                        fringe[(nx, ny)] = (ncost, nmd)

###############################################################################

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [40]
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
