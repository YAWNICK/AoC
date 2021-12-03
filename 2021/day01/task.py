import os


def compute1(s: str):
    lines = s.splitlines()
    res = 0
    curr = None
    for line in lines:
        if curr is not None:
            if int(line) > curr:
                res += 1
        curr = int(line)
    return res


def compute2(s: str):
    lines = s.splitlines()
    res = 0
    curr1, curr2, curr3 = None, None, None
    for line in lines:
        if None not in [curr1, curr2, curr3]:
            if int(line) + curr1 + curr2 > curr1 + curr2 + curr3:
                res += 1
        curr3 = curr2
        curr2 = curr1
        curr1 = int(line)

    return res

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
    print("Part 1:", compute1(inp))
    print("Part 2:", compute2(inp))

if __name__ == "__main__":
    main()
