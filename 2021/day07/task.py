import os

def compute(s: str, part: int):
    s = s.strip()
    s = list(map(int, s.split(',')))
    ress = []
    for x in range(max(s)):
        res = 0
        for i in s:
            res += tr(abs(x-i)) if part == 2 else abs(x-i)
        ress.append(res)
    return min(ress)
    #return ress.index(min(ress))

def tr(x):
    return x*(x+1)//2
    #return sum(range(x+1))

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
    print("Part 1:", compute(inp, 1))
    print("Part 2:", compute(inp, 2))

if __name__ == "__main__":
    main()
