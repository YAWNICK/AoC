import os
from copy import deepcopy
from pprint import pprint

Depth = 4
SlotInds = {'A':2,'B':4,'C':6,'D':8}
Costs = {'A':1,'B':10,'C':100,'D':1000}

def new_states(b, cost, mvs):
    moves = []
    # preparation
    hps = dict()
    for v,y in SlotInds.items():
        x = 0
        while b[x+1][y] == '.':
            x += 1
        ready = True
        for xx in range(x+1,Depth+1):
            if b[xx][y] != v:
                ready = False
        hps[v] = (y,x,ready)
    # outgoing moves
    for v, (py,px,ready) in hps.items():
        #py, px, ready = *data
        if px == Depth:
            continue
        x = px+1
        #piece = b[x][py]
        for y in [0,1,3,5,7,9,10]:
            if b[0][y] != '.':
                continue
            if b[0][min(py,y):max(py,y)+1].count('.') < abs(py-y)+1:
                continue
            moves.append((x,py,0,y,(x+abs(py-y))*Costs[b[x][py]]))
    # returniing moves
    for py in [0,1,3,5,7,9,10]:
        v = b[0][py]
        if v == '.':
            continue
        slot = SlotInds[v]
        if b[0][min(py+1,slot):max(py,slot)+1].count('.') < abs(py-slot):
            continue
        y, x, ready = hps[v]
        if not ready:
            continue
        moves.append((0,py,x,slot,(x+abs(py-slot))*Costs[v]))
    # generate new states
    states = []
    for x1,y1,x2,y2,c in moves:
        nb = deepcopy(b)
        nb[x2] = nb[x2][:y2] + nb[x1][y1] + nb[x2][y2+1:]
        nb[x1] = nb[x1][:y1] + '.' + nb[x1][y1+1:]
        states.append((nb,cost+c,mvs+[(y1,y2)]))
    return states

def isfinal(b):
    line = '##A#B#C#D##'
    if b[1] == line and b[2] == line and b[3] == line and b[4] == line:
        return True
    return False

def compute(s: str):
    b = ['...........',
         '##C#B#A#D##',
         '##D#C#B#A##',
         '##D#B#A#C##',
         '##B#C#D#A##',
         '###########']
    seen = dict()
    fringe = [(b,0,[])]
    noticed = False
    #for i in range(5):
    tsd = 1000
    while True:
        fe = min(fringe, key=lambda s: s[1])
        fringe.remove(fe)
        state, cost, moves = fe[0], fe[1], fe[2]
        if cost > tsd:
            print(tsd)
            tsd += 1000
        if isfinal(state):
            print("Found solution!")
            print(moves)
            return cost
        tstate = tuple(state)
        if tstate in seen:
            if seen[tstate] <= cost:
                continue
        seen[tstate] = cost
        fringe += new_states(state, cost, moves)
    return 

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
