import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    res = 0
    for line in lines:
        ns = list(map(int, line.split()))
        safe = False
        for i in range(len(ns)):
            nns = ns.copy()
            nns.pop(i)
            ds = [a - b for a, b in zip(nns[1:], nns)]
            if 0 in ds:
                continue
            if max(ds)<=3 and min(ds)>=1 or max(ds)<=-1 and min(ds)>=-3:
                #res += 1
                safe= True
                break
        if safe:
            res += 1
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
    print(compute(inp))

if __name__ == "__main__":
    main()
