import os

def compute(s: str):
    lines = s.splitlines()
    
    seeds, lines = lines[0], lines[3:]
    seeds = list(map(int, seeds[7:].split()))
    #ranges = [list(range(seeds[i], seeds[i+1])) for i in range(0, len(seeds)//2, 2)]
    seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    for _ in range(7):
        si = lines.index('')
        m, lines = lines[:si], lines[si+2:]
        m = [list(map(int, line.split())) for line in m]
        m.sort(key=lambda x: x[1])
        if m[0][1] != 0:
            m = [[0, 0, m[0][1]]] + m
        for rule in m:
            ri, ro = rule[1], rule[1]+rule[2]
            for ind in range(len(seeds)):
                i, o = seeds[ind][0], seeds[ind][0]+seeds[ind][1]
                if i >= ro or o <=ri:
                    continue
                mi, mo = i, o
                if i < ri:
                    seeds.append((i, ri-i))
                    mi = ri
                if o > ro:
                    seeds.append((ro, o-ro))
                    mo = ro
                seeds.append((mi, mo-mi))
                seeds.remove((i, o-i))
        seeds = list(map(lambda s: (mapn(s[0], m), s[1]), seeds))
    res = min(seeds, key=lambda x: x[0])
    print(res)
    return res

def mapn(n, m):
    l = 0
    r = len(m)-1
    while l != r:
        i = (l+r)//2
        if n < m[i][1]:
            r = i
        else:
            l = i
            if r-l==1:
                if n >= m[r][1]:
                    l = r
                else:
                    r = l
    return m[l][0]+(n-m[l][1]) if m[l][2]> n-m[l][1] else n

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [35]
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
