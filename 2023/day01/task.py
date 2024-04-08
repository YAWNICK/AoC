import os

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    data = lines
    res = 0
    ns = ['1','2','3','4','5','6','7','8','9','one','two','three','four','five','six','seven','eight','nine']
    for i in data:
        a = None
        for j in range(len(i)):
            for ii, c in enumerate(ns):
                if i[j:].startswith(c):
                    a = ii+1 if ii <= 8 else ii-8
                    break
            if a is not None:
                break
        b = None
        for j in range(len(i), 0, -1):
            for ii, c in enumerate(ns):
                if i[:j].endswith(c):
                    b = ii+1 if ii <= 8 else ii-8
                    break
            if b is not None:
                break
        res += a*10+b
    return res

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [281]
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
