import os


def compute1(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    for l in lines:
        for s in lines:
            if int(l) + int(s) == 2020:
                    return int(l) * int(s)

def compute2(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    for l in lines:
        for s in lines:
            for t in lines:
                if int(l) + int(s) + int(t) == 2020:
                    return int(l) * int(s) * int(t)


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
