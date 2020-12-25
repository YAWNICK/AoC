import os

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    pc1 = int(lines[0])
    pc2 = int(lines[1])
    l1 = None
    l2 = None
    isn = 7
    found = 0
    v = 1
    i = 1
    while found < 2:
        v *= isn
        v = v % 20201227
        if v == pc1:
            l1 = i
            found += 1
        if v == pc2:
            l2 = i
            found += 1
        i += 1
    return transform(pc2, l1)

def transform(sn, ln):
    v = 1
    for i in range(ln):
        v *= sn
        v = v % 20201227
    return v

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [14897079]
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
