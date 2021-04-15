import os

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    totals = [0, 0, 0, 0, 0]
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    w = len(lines[0])
    h = len(lines)
    for i, (r, d) in enumerate(slopes):
        pos = [0,0]
        while pos[1] < h:
            if lines[pos[1]][pos[0]] == '#':
                totals[i] += 1
            pos[0] = (pos[0] + r) % w
            pos[1] += d
    res1 = totals[1]  # for slope (3, 1)
    res2 = 1
    for t in totals:
        res2 *= t
    return (res1, res2)

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
    res = compute(inp)
    print(f"Part 1: {res[0]}")
    print(f"Part 2: {res[1]}")

if __name__ == "__main__":
    main()
