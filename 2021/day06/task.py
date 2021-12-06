import os

def compute(s: str, days: int):
    s = s.strip()
    ss = map(int, s.split(','))
    G = [0]*9
    for s in ss:
        G[s] += 1
    for i in range(days):
        o = G[0]
        G = G[1:] + [o]
        G[6]+= o
    return sum(G)

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
    print("Part 1:", compute(inp, 80))
    print("Part 2:", compute(inp, 256))

if __name__ == "__main__":
    main()
