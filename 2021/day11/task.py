import os

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def compute1(s: str):
    lines = s.splitlines()
    l = [list(map(int, line)) for line in lines]
    res = 0
    for i in range(100):
        l, fs = step(l)
        res += fs
    return res

def compute2(s: str):
    lines = s.splitlines()
    l = [list(map(int, line)) for line in lines]
    res = 0
    while True:
        l, fs = step(l)
        res += 1
        if fs == 100:
            return res

def step(l):
    l = [list(map(lambda x: x+1, line)) for line in l]
    flashed = set()
    while max(sum(l, [])) > 9:
        for i, line in enumerate(l):
            for j, n in enumerate(line):
                if n > 9 and (i,j) not in flashed:
                    flashed.add((i,j))
                    for di, dj in dirs:
                        if 0 <= i+di <= 9 and 0 <= j+dj <= 9:
                            l[i+di][j+dj] += 1
                    # The following line ensures that already flashed octopi
                    # never reach a value of >9 again during the while loop,
                    # which is necessary for the while condition to work.
                    l[i][j] = 0
    for i, j in flashed:
        l[i][j] = 0
    return l, len(flashed)

###############################################################################

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
    #run_tests()
    inp = read_input("input.txt")
    print("Part 1:", compute1(inp))
    print("Part 2:", compute2(inp))

if __name__ == "__main__":
    main()
