import os
from pprint import pprint
from collections import defaultdict

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    Ps = []
    for line in lines:
        p, d = line.split(' @ ')
        p = list(map(int, p.split(', ')))
        d = list(map(int, d.split(', ')))
        Ps.append(p+d)
    # TESTING
    #Ps = Ps[:2]
    # TESTING
    Pslen = len(Ps)
    print(Pslen)
    D = defaultdict(int)
    for i in range(Pslen - 1):
        print('position', i)
        j = i+1
        Ps1 = [(x+i*dx, y+i*dy, z+i*dz) for x,y,z,dx,dy,dz in Ps]
        Ps2 = [(x+j*dx, y+j*dy, z+j*dz) for x,y,z,dx,dy,dz in Ps]
        for ii in range(len(Ps1)):
            for jj in range(len(Ps2)):
                if ii == jj:
                    continue
                x1, y1, z1 = Ps1[ii]
                x2, y2, z2 = Ps2[jj]
                D[(x2-x1, y2-y1, z2-z1)] += 1
    print(len(DD))
    tops = sorted(D.items(), key=lambda x: x[1])[:20]
    for t in tops:
        print(t)
    return None 

def colltest(x1, y1, z1, dx1, dy1, dz1, x2, y2, z2, dx2, dy2, dz2):
    pts1 = []
    for i in range(50):
        pts1.append((x1+i*dx1, y1+i*dy1, z1+i*dz1))
    pprint(pts1)
    for j in range(50):
        pt2 = (x2+i*dx2, y2+i*dy2, z2+i*dz2)
        if pt2 in pts1:
            return pt2, pts1.index(pt2), j
    return None, None, None

def collision(x1, y1, z1, dx1, dy1, dz1, x2, y2, z2, dx2, dy2, dz2):
    # TODO prevent zerodiv error
    #print('----new coll check -----')
    denom = dy2 - (dx2/dx1)*dy1
    #print(denom)
    if denom == 0:
        return None
    m2 = (y1 + (x2/dx1)*dy1 - (x1/dx1)*dy1 - y2) / (dy2 - (dx2/dx1)*dy1)
    m1 = (x2 + m2*dx2 - x1) / dx1
    #assert x1 + m1*dx1 == x2 + m2*dx2
    #print('Y Y', y1 + m1*dy1, y2 + m2*dy2)
    #assert y1 + m1*dy1 == y2 + m2*dy2
    #print(m1, m2)
    #print(z1 + m1*dz1, z2 + m2*dz2)
    #if not z2 + m2*dz2 - EPS <= z1 + m1*dz1 <= z2 + m2*dz2 + EPS:
    #    print('z coordinate mismatch')
    #    return None
    # TODO potentially check filter conditions here
    if m1 < 0 or m2 < 0:
        #print('behind start of ray')
        return None
    p1 = x1 + m1*dx1
    p2 = y1 + m1*dy1
    #p3 = z1 + m1*dz1

    return p1, p2 #, p3




def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [0]
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
