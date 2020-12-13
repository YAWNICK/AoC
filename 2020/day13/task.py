import os
import re

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    
    guess = int(lines[0])
    bs = list(map(int, re.findall("[0-9]+", lines[1])))
    # part 1:
    #left = list(map(lambda x: x - (guess % x), bs))
    #print(bs)
    #print(left)
    # ... then figure it out by looking at it

    # part 2:
    ind = list(re.findall("[0-9a-z]+", lines[1]))
    indices = list(map(lambda x: ind.index(str(x)), bs))
    u = {}
    for n in bs:
        u[n] = []
    cnt = 0
    step = 1
    yes = 0
    while yes < len(bs):
        yes = 0
        cnt += step
        for i, n in enumerate(bs):
            if (cnt + indices[i]) % n == 0:
                yes += 1
                if len(u[n]) == 0:
                    u[n].append(cnt)
                elif len(u[n]) == 1:
                    u[n].append(cnt)
                    step = cnt - u[n][0]
            else:
                break
    return cnt

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [1068781]
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
    print(compute(inp))

if __name__ == "__main__":
    main()
