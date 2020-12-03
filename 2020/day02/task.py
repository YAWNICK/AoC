import os

def count(s, c):
    total = 0
    for ch in s:
        if ch == c:
            total +=1
    return total

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    total = 0
    for line in lines:
        rule, pw = line.split(':')
        pw = pw.strip()
        mm, n = rule.split(' ')
        mi, ma = mm.split('-')
        ## part 1
        #if count(pw, n) >= int(mi) and count(pw, n) <= int(ma):
        #    total += 1
        ## part 2
        if pw[int(ma)-1] == n or pw[int(mi)-1] == n:
            total += 1
        if pw[int(ma)-1] == n and pw[int(mi)-1] == n:
            total -= 1

    return total

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
