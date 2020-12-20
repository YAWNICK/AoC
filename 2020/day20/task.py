import os
from functools import reduce

def edge_to_bin(s):  # hash function for an edge
    binstr = s.replace('#', '1').replace('.', '0')
    return [int(bin(eval('0b'+binstr)), 2), int(bin(eval('0b'+binstr[::-1])), 2)]

def compute(s: str):
    # monster coordinates from its top left corner
    mcos = [(0,18), (1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18),
            (1,19), (2,1), (2,4), (2,7), (2,10), (2,13), (2,16)]
    tiles = s.split('\n\n')
    cvals = {}  # <int, [[int, int]]*4> maps tile number to the two hashes of all of its edges 
    allvals = []  # all edge hashes of all tiles (outer edges appear only once)
    tconts = {}  # <int, [str]> tile contents
    for tile in tiles:  # now fill cvals, allvals and tconts
        t = tile.splitlines()
        tn = int(t[0][5:-1])
        tconts[tn] = t[1:]
        sides = []
        sides.append(edge_to_bin(t[1]))  # top edge
        sides.append(edge_to_bin(t[-1]))  # bottom edge
        for i in range(2):  # right and left edge
            sidestr = ''
            for j in range(len(t[1:])):
                sidestr += t[j+1][i-1]
            sides.append(edge_to_bin(sidestr))
        cvals[tn] = sides
        allvals += list(reduce(list.__add__, sides))
    # find corners
    corners = []
    for tn, sides in cvals.items():
        nc = 0  # number of edges that have no correspondant
        for i, side in enumerate(sides):
            if allvals.count(side[0]) == 1 and allvals.count(side[1]) == 1:
                nc += 1
                sides[i] = [-1, -1]  # somehow mark this edge to be able to skip it later
        if nc >= 2:
            corners.append(tn)
    # part 1: prod or corners
    print("Part 1:", reduce(int.__mul__, corners))
    ids = [[]]  # correct position of tiles in the overall image
    tops = {}   # maps tiles to their correct orientation in the overall image
    '''
    The orientation of a tile is defined by a 3 tuple. 
    - first: rotate the tile til the specified side faces up (u,d,r,l)
      correspond to (0,1,2,3)
    - second: boolean(1/0): does the tile need to be flipped?
    - third: if it needs to be flipped, then along which axis? (either 'r' or 't')
    '''
    # begin with the first corner in the bottom left spot and manually orient it
    tops[1453] = [3, 0]
    ids[0].append(1453)
    # the dock variables are the edge hashes which need to match the currently
    # looked at tile to the right and to the top. There is a convention which
    # of the two directions in which an edge can be read is specified in the
    # dock variables: for right it's downwards, for top it's to the right; when
    # looking at the tile in its correct orientation
    cdock_r = cvals[1453][0][0]  # 953
    cdock_t = cvals[1453][3][1]  # 81
    for i in range(11):  # fill the bottom row starting from the first edge
        tn, top, cdock_top, cdock_right = match(cdock_r, 'r', cvals)
        ids[0].append(tn)
        tops[tn] = top
        cvals.pop(tn)
        cdock_r = cdock_right
    for i in range(11):  # fill all rows above, alwas starting with the left edge tile
        ids.append([])
        tn, top, cdock_top, cdock_right = match(cdock_t, 't', cvals)
        ids[i+1].append(tn)
        tops[tn] = top
        cvals.pop(tn)
        cdock_r = cdock_right
        cdock_t = cdock_top
        for j in range(11):  # continue to the right from the edge tile
            tn, top, cdock_top, cdock_right = match(cdock_r, 'r', cvals)
            ids[i+1].append(tn)
            tops[tn] = top
            cvals.pop(tn)
            cdock_r = cdock_right
    plane = []  # the actual image pieced together by the tiles
    for row in ids:
        lines = ['']*8
        for tile in row:
            t = iso_tile(tconts[tile], tops[tile])  # orient the tile
            t = strip_tile(t)
            for lineind in range(8):
                lines[lineind] += t[lineind]
        plane = lines + plane
    # apparently three left rotations and a vertical flip bring the plane in
    # the correct orientation to search for monsters
    plane = mirr(rotl(rotl(rotl(plane))), 't')
    total = 0  # total number of monsters
    for i in range(len(plane) - 3):  # 3 = height of monster
        for j in range(len(plane[0]) - 19):  # 19 = length of monster
            there = True
            for mc in mcos:
                if plane[i+mc[0]][j+mc[1]] != '#':
                    there = False
                    break
            if there == True:
                total += 1
    cnt = 0
    for line in plane:
        cnt += line.count('#')
    return cnt - (total * 15)  # a Monster consists of 15 #s

def strip_tile(tile):
    new = []
    for line in tile[1:-1]:
        new.append(line[1:-1])
    return new

def iso_tile(tile, top):
    new = tile.copy()
    t = top[0]
    if t == 2:
        new = rotl(tile)
    elif t == 1:
        new = rotl(rotl(tile))
    elif t == 3:
        new = rotl(rotl(rotl(tile)))
    if top[1] == 1:
        new = mirr(new, top[2])
    return new

def mirr(tile, direction):
    if direction == 't':
        for i, row in enumerate(tile):
            tile[i] = tile[i][::-1]
    else:
        tile.reverse()
    return tile

def rotl(tile):
    new = []
    for i in range(len(tile[0]) - 1, -1, -1):
        s = ''
        for j in range(len(tile)):
            s += tile[j][i]
        new.append(s)
    return new

def match(cdock: int, mdir: str, cvals):
    found = False
    for tn, sides in cvals.items():
        for si, side in enumerate(sides):
            if side == [-1, -1]:
                continue
            for soi, ori in enumerate(side):
                if ori == cdock:
                    found = True
                    if mdir == 'r':
                        if si == 0:
                            if soi == 0:
                                return tn, [2, 1, 'r'], sides[3][0], sides[1][0]
                            else:
                                return tn, [2, 0, 'r'], sides[2][0], sides[1][1]
                        elif si == 1:
                            if soi == 0:
                                return tn, [3, 0, 'r'], sides[3][1], sides[0][0]
                            else:
                                return tn, [3, 1, 'r'], sides[2][1], sides[0][1]
                        elif si == 2:
                            if soi == 0:
                                return tn, [1, 1, 'r'], sides[0][1], sides[3][0]
                            else:
                                return tn, [1, 0, 'r'], sides[1][1], sides[3][1]
                        else:  # si == 3
                            if soi == 0:
                                return tn, [0, 0, 'r'], sides[0][0], sides[2][0]
                            else:
                                return tn, [0, 1, 'r'], sides[1][0], sides[2][1]
                    else:  # mdir == 't'
                        if si == 0:
                            if soi == 0:
                                return tn, [1, 1, 't'], sides[1][0], sides[2][1]
                            else:
                                return tn, [1, 0, 't'], sides[1][1], sides[3][1]
                        elif si == 1:
                            if soi == 0:
                                return tn, [0, 0, 't'], sides[0][0], sides[2][0]
                            else:
                                return tn, [0, 1, 't'], sides[0][1], sides[3][0]
                        elif si == 2:
                            if soi == 0:
                                return tn, [3, 1, 't'], sides[3][0], sides[1][0]
                            else:
                                return tn, [3, 0, 't'], sides[3][1], sides[0][0]
                        else:  # si == 3
                            if soi == 0:
                                return tn, [2, 0, 't'], sides[2][0], sides[1][1]
                            else:
                                return tn, [2, 1, 't'], sides[2][1], sides[0][1]

# setup

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
    print("Part 2:", compute(inp))

if __name__ == "__main__":
    main()
