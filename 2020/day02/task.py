import os

def count(s, c):  # count occurrences of char c in string s
    total = 0
    for ch in s:
        if ch == c:
            total +=1
    return total

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    total1, total2 = 0, 0
    for line in lines:
        rule, pw = line.split(': ')
        mm, n = rule.split(' ')
        mi, ma = mm.split('-')
        # part 1
        c = count(pw, n)
        if c >= int(mi) and c <= int(ma):
            total1 += 1
        # part 2
        if pw[int(ma)-1] == n or pw[int(mi)-1] == n:
            total2 += 1
        if pw[int(ma)-1] == n and pw[int(mi)-1] == n:
            total2 -= 1

    return (total1, total2)

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
