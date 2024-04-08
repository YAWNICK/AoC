import os

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    R, G, B = 12, 13, 14
    M = {'red': R, 'green':G, 'blue':B}
    res = 0
    for line in lines:
        g, line = line.split(': ')
        gid = int(g[5:])
        sets = line.split('; ')
        M = {'red': 0, 'green':0, 'blue':0}
        for s in sets:
            for p in s.split(', '):
                n, c = p.split()
                n = int(n)
                if n > M[c]:
                    M[c] = n
        res += M['green']*M['red']*M['blue']
        #if all(map(lambda s: valid(s, M), sets)):
        #    res.append(gid)
            
    return res


def valid(s, M):
    for p in s.split(', '):
        n, c = p.split()
        n = int(n)
        if n > M[c]:
            return False
    return True


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
