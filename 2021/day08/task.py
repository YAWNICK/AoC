import os, copy

D = {0: set('abcefg'), 1: set('cf'), 2: set('acdeg'), 3: set('acdfg'), 
     4: set('bcdf'), 5: set('abdfg'), 6: set('abdefg'), 7: set('acf'), 
     8: set('abcdefg'), 9: set('abcdfg')}

def compute1(s):
    lines = s.splitlines()
    res = 0
    for line in lines:
        i, o = line.split(' | ')
        o = o.split(' ')
        for c in o:
            if len(c) in [2, 3, 4, 7]:
                res += 1
    return res

def compute2(s: str):
    lines = s.splitlines()
    result = 0
    for line in lines:
        i, o = line.split(' | ')
        o = o.split(' ')
        i = i.split(' ')
        M = {c: '' for c in 'abcdefg'}
        c0, c1, c2, c3, c4, c5, c6, c7, c8, c9 = [None]*10
        l5, l6 = [], []
        for n in i:
            ln = len(n)
            if ln == 2:
                c1 = set(n)
            elif ln == 3:
                c7 = set(n)
            elif ln == 4:
                c4 = set(n)
            elif ln == 7:
                c8 = set(n)
            elif ln == 5:
                l5.append(set(n))
            elif ln == 6:
                l6.append(set(n))
        for i, s in enumerate(l6):
            if c1.issubset(s):
                if c4.issubset(s):
                    c9 = s
                else:
                    c0 = s
            else:
                c6 = s
        for i, s in enumerate(l5):
            if c1.issubset(s):
                c3 = s
            else:
                if len(c6.difference(s)) == 1:
                    c5 = s
                else:
                    c2 = s
        M['a'] = c7.difference(c1).pop()
        (h := c9.difference(c4)).discard(M['a'])
        M['g'] = h.pop()
        M['b'] = c4.difference(c3).pop()
        (h := c4.difference(c1)).discard(M['b'])
        M['d'] = h.pop()
        M['c'] = c1.difference(c6).pop()
        (h := c1.copy()).discard(M['c'])
        M['f'] = h.pop()
        M['e'] = c6.difference(c5).pop()
        
        rM = {v:k for k, v in M.items()}
        
        d = ''
        for n in o:
            cs = set(map(lambda x: rM[x], n))
            for k, num in D.items():
                if cs == num:
                    d += str(k)
                    break
        result += int(d)
        
    return result

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [61229, 5353]
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
    print("Part 1:", compute1(inp))
    print("Part 2:", compute2(inp))

if __name__ == "__main__":
    main()
