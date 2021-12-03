import os

def compute1(s: str):
    lines = s.splitlines()
    x, y = 0, 0
    for line in lines:
        dir, val = line.split()
        val = int(val)
        if dir == "forward":
            x += val
        elif dir == "up":
            y -= val
        elif dir == "down":
            y += val
    return x * y

def compute2(s: str):
    lines = s.splitlines()
    x, y, aim = 0, 0, 0
    for line in lines:
        dir, val = line.split()
        val = int(val)
        if dir == "forward":
            x += val
            y += val * aim
        elif dir == "up":
            aim -= val
        elif dir == "down":
            aim += val
    return x * y

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
