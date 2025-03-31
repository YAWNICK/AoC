import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    res = 0
    for line in lines:
        #print(line)
        t, xs = line.split(': ')
        t = int(t)
        xs = list(map(int, xs.split()))
        lxs = len(xs)
        
        if valid2(xs, set([t])):
            res += t

        #if lxs >= 12:
        #    print("long", lxs)
        #    if valid(xs[:-1], [0]*(lxs-2), t-xs[-1]):
        #        res += t
        #    elif t % xs[-1] == 0 and valid(xs[:-1], [0]*(lxs-2), t // xs[-1]):
        #        res += t
        #else:
        #    if valid(xs, [0]*(len(xs)-1), t):
        #        res += t
    print(res)
    return res

def valid2(xs, tl):
    if len(xs) == 1:
        #print("# opts", len(tl))
        return xs[0] in tl
    ts = set()
    c = xs[-1]
    for t in tl:
        if t >= c:
            ts.add(t-c)
        if t % c == 0:
            ts.add(t // c)
        if str(t).endswith(str(c)):
            if t != c:
                ts.add(int(str(t)[:-1*len(str(c))]))
            if t == c and all([x == 1 for x in xs[:-1]]):
                ts.add(1)
    return valid2(xs[:-1], ts)

def valid(xs, ops, t):
    r = calc(xs, ops)
    if r == t:
        return True
    if r > t:
        return False
    if 0 not in ops:
        return False
    oops = ops[:]
    for i in range(ops.count(0)):
        ind = oops.index(0)
        vops = ops[:]
        vops[ind] = 1
        oops[ind] = 1
        if valid(xs, vops, t):
            return True
    return False

def calc(xs, ops):
    s = xs[0]
    for x, op in zip(xs[1:], ops):
        if op == 0:
            s += x
        else:
            s *= x
    return s

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
