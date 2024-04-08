import os
from collections import defaultdict

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    ylen = len(lines)
    G = defaultdict(list) 
    y, x = 0, 1
    py, px = -1, 0
    gy, gx = y, x
    Q = [(y, x, py, px)]
    while Q:
        gy, gx, gpy, gpx = Q.pop(0)
        if gy == ylen-1:
            continue
        gds = []
        for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if dy == gpy and dx == gpx:
                continue
            ny, nx = gy+dy, gx+dx
            #print(gy, gx, ny, nx)
            if lines[ny][nx] != '#':
                gds.append((dy, dx))
        assert not (len(gds) > 1 and lines[gy][gx] in '<>^v')
        ngs = []
        for gdy, gdx in gds:
            y, x = gy+gdy, gx+gdx
            py, px = -gdy, -gdx
            #direction = 0  # 0: both ways, 1: only with me, -1: only against me
            ngy, ngx = None, None  # if thexy stay none, it was a dead end
            pathlen = 1
            while True:
                if y == ylen-1:
                    ngy, ngx = y, x
                    break
                ds = []
                for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    if dy == py and dx == px:
                        continue
                    ny, nx = y+dy, x+dx
                    if lines[ny][nx] != '#':
                        ds.append((dy, dx))
                lds = len(ds)
                if lds == 0:
                    break
                if lds > 1:
                    ngy, ngx = y, x
                    break
                assert lds == 1
                #if direction == 0:
                #direction = update_direction(lines[y][x], py, px)
                #if direction == -1:
                #    break
                y, x = y+ds[0][0], x+ds[0][1]
                py, px = -ds[0][0], -ds[0][1]
                pathlen += 1
            if ngy is None:
                continue
            if (ngy, ngx, pathlen) in G[(gy, gx)]:
                continue
            G[(gy, gx)].append((ngy, ngx, pathlen))
            Q.append((ngy, ngx, py, px))
            #if direction == 0:
                #print('DIRECTION 0', gy, gx, ngy, ngx)
            G[(ngy, ngx)].append((gy, gx, pathlen))
    print('graph created')
    for pos, nb in G.items():
        print(pos, nb)
    res = walk(G, 0, 1, {(0, 1)}, 0, ylen-1)
    print('REULT', res)
    return


def walk(G, y, x, visited, dist, endy):
    if y == endy:
        return dist
    md = 0
    for nby, nbx, nbd in G[(y, x)]:
        if (nby, nbx) in visited:
            continue
        nvisited = visited.copy()
        nvisited.add((nby, nbx))
        md = max(md, walk(G, nby, nbx, nvisited, dist + nbd, endy))
    return md


def update_direction(symbol, py, px):
    if symbol == '>':
        if px == -1:
            return 1
        if px == 1:
            return -1
    if symbol == 'v':
        if py == -1:
            return 1
        if py == 1:
            return -1
    return 0


def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [94]
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
