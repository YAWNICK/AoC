import os
import re

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    rules = lines[:20]
    myt = list(map(int, lines[22].split(',')))
    ts = lines[25:]  # tickets
    rs = {}  # <rule name, [[rule1 lower, rule1 upper], [rule2 lower, rule2 upper]]>
    for line in rules:
        rg = re.search("(.*): ([0-9]+-[0-9]+) or ([0-9]+-[0-9]+)", line)
        rn = rg.group(1)
        r1 = rg.group(2)
        r2 = rg.group(3)
        rs[rn] = [list(map(int, r1.split('-'))), list(map(int, r2.split('-')))]
    rlen = len(rs.keys())  # number of rules
    ts = list(map(lambda x: list(map(int, x.split(','))), ts))
    invalids = []  # invalid numbers
    new_ts = []  # all valid tickets
    for t in ts:
        ns_missed = 0
        for n in t:
            rules_missed = 0
            for r in rs.values():
                if not satisfies(r, n):
                    rules_missed += 1
            if rules_missed == rlen:
                invalids.append(n)
                ns_missed += 1
        if ns_missed == 0:
            new_ts.append(t)
    print("Part 1:", sum(invalids))
    dist = {}  # <position, rule name>
    possr = {}  # <position, [rule name]>
    # possible rules
    for pos in range(rlen):
        for rn in rs.keys():
            if rmachtespos(rs[rn], pos, new_ts):
                possr.setdefault(pos, []).append(rn) 
    # rule distribution
    for i in range(rlen):
        pos = None
        for p, rns in possr.items():
            if len(rns) == 1:
                dist[p] = rns[0]
                pos = p
                break
        for p, rns in possr.items():
            if dist[pos] in rns:
                rns.remove(dist[pos])
    prod = 1
    for p, rn in dist.items():
        if 'departure' in rn:
            prod *= myt[p]
    return prod

def rmachtespos(rval, pos, ts):
    for t in ts:
        if not satisfies(rval, t[pos]):
            return False
    return True

def satisfies(rval, n):
    if n < rval[0][0] or n > rval[1][1] or (rval[0][1] < n < rval[1][0]):
        return False
    return True

# setup

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [4]
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
    print("Part 2:", compute(inp))

if __name__ == "__main__":
    main()
