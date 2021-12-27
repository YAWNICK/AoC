import os
import re
import math

def parse(line):
    return eval(line.replace('[', '(').replace(']', ')'))

def explode(rs: str, i: int):
    #print("Explode:", rs)
    lrs = len(rs)
    idelim = rs.index(',', i)
    iend = rs.index(')', idelim)
    a = int(rs[i+1:idelim])
    b = int(rs[idelim+1:iend])
    ml = re.search('\d+', rs[:i][::-1])
    #ila = i
    #while ila >= 0:
    #    if rs[ila] not in '(),':
    #        break
    #    ila -= 1
    if ml:
        liend, listart = ml.span()
        nl = int(rs[i-listart:i-liend])
        rsl = rs[:i-listart] + str(nl+a) + rs[i-liend:i]
    else:
        rsl = rs[:i]
    mr = re.search('\d+', rs[iend+1:])
    #irb = iend
    #while irb < lrs:
        #print(irb)
    #    if rs[irb] not in '(),':
    #        break
    #    irb += 1
    if mr:
        ristart, riend = mr.span()
        nr = int(rs[iend+1+ristart:iend+1+riend])
        #print(nr)
        rsr = rs[iend+1:iend+1+ristart] + str(nr+b) + rs[iend+1+riend:]
    else:
        rsr = rs[iend+1:]
    return rsl + '0' + rsr

def split(rs, i, j):
    #print("Split:  ", rs)
    n = int(rs[i:j])
    a = math.floor(n / 2)
    b = math.ceil(n / 2)
    return rs[:i] + f'({a},{b})' + rs[j:]

def add(a, b):
    r = (a, b)
    rs = str(r).replace(' ', '')
    todo = True
    while todo:
        if re.search('[0-9][0-9][0-9]', rs):
            print(rs)
            return
        todo = False
        rsl = len(rs)
        i, d = 0, 0
        while i < rsl:
            d += 1 if rs[i] == '(' else 0
            d -= 1 if rs[i] == ')' else 0
            if d == 5:
                break
            i += 1
        if d == 5:
            rs = explode(rs, i)
            todo = True
            continue
        # split
        m = re.search('[1-9][0-9]', rs)
        if m is None:
            continue
        rs = split(rs, *m.span())
        todo = True
        
    return eval(rs)
   
def magnitude(r):
    if isinstance(r, int):
        return r
    return 3*magnitude(r[0])+2*magnitude(r[1])

def compute(s: str):
    lines = s.splitlines()
    ns = [parse(line) for line in lines]
    #n = ns[0]
    #print(n)
    #print(ns[1])
    #return
    #for na in ns[1:]:
    #    n = add(n, na)
        #print('NEW VALUE:', n)
    #print(magnitude(n))
    m = 0
    for na in ns:
        for nb in ns:
            res = magnitude(add(na, nb))
            if res > m:
                m = res
    print(m)
    return m

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [1]
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
