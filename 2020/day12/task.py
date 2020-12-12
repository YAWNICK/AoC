import os

dirs = {'N': (1,0), 'S':(-1,0), 'E':(0,1), 'W':(0,-1)}
D = ['N', 'E', 'S', 'W']

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    h = 0
    v = 0
    
    # part 1
    f = 'E'
    # part 2
    wh = 10
    wv = 1

    for line in lines:
        d = line[0]
        n = int(line[1:])
        if d in D:
            # part 1
            #h += dirs[d][1] * n
            #v += dirs[d][0] * n
            # part 2
            wh += dirs[d][1] * n
            wv += dirs[d][0] * n
        elif d == 'F':
            # part 1
            #h += dirs[f][1] * n
            #v += dirs[f][0] * n
            # part 2
            for i in range(n):
                h += wh
                v += wv
        elif d == 'R':
            # part 1
            #f = D[(D.index(f) + (n // 90)) % 4]
            # part 2
            for i in range(n // 90):
                wh, wv = wv, -wh
        elif d == 'L':
            # part 1
            #f = D[(D.index(f) - (n // 90)) % 4]
            # part 2
            for i in range(n // 90):
                wh, wv = -wv, wh
    
    return abs(h) + abs(v)

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
