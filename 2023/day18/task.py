import os

def compute(s: str):
    lines = s.splitlines()
    V = []
    y = 0
    x = 0
    D = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    for line in lines:
        # Part 1
        #d, nsteps, color = line.split()
        #nsteps = int(nsteps)
        # Part 2
        code = line.split()[-1][2:-1]
        nsteps, d = int(code[:-1], 16), code[-1]
        d = 'RDLU'[int(d)]
        
        dy, dx = D[d]
        s = '|' if d in 'UD' else '-'
        if d in 'UD':
            yend = y + nsteps*dy
            V.append((min(y, yend), x, max(y, yend), x))
        y += dy*nsteps
        x += dx*nsteps
    V.sort(key=lambda seg: seg[1])
    area = 0
    cut = []
    x = 0
    while V:
        y1, nx, y2, _ = V.pop(0)
        for py1, py2, in cut:
            area += (py2-py1+1)*(nx-x)
        add, rem = [], []
        coll = []
        inside = None
        for cy1, cy2 in cut:
            if y1 in (cy1, cy2) or y2 in (cy1, cy2):
                coll.append((cy1, cy2))
            if y1 > cy1 and y2 < cy2:
                inside = (cy1, cy2)
        colllen = len(coll)
        if colllen == 0:
            if inside:
                add = [(inside[0], y1), (y2, inside[1])]
                rem = [inside]
                area += y2-y1-1
            else:
                add = [(y1, y2)]
        elif colllen == 1:
            cy1, cy2 = coll[0]
            if y1 < cy1 or y2 > cy2:
                add = [(min(y1, cy1), max(y2, cy2))]
            elif y1 == cy1 and y2 != cy2:
                add = [(y2, cy2)]
                area += y2-y1
            elif y2 == cy2 and y1 != cy1:
                add = [(cy1, y1)]
                area += y2-y1
            elif y1 == cy1 and y2 == cy2:
                area += y2-y1+1
            rem = [(cy1, cy2)]
        elif colllen == 2:
            add = [(min(coll[0][0], coll[1][0]), max(coll[0][1], coll[1][1]))]
            rem = [coll[0], coll[1]]
        for a in add:
            cut.append(a)
        for r in rem:
            cut.remove(r)
        x = nx
    print(area)
    return area

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [62]
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
