import os

# helpful print method
def p(s):
    for line in s:
        print(line)

# sum of occurrences of a given state in sudrroundings of a given seat
def sis(s, r, c, status):
    su = 0
    for k, l in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1,
        -1), (1, 0), (1, 1)]:
        cor = r + k
        coc = c + l
        if cor < 0 or cor >= len(s) or coc < 0 or coc >= len(s[0]):
            continue
        while s[cor][coc] == '.':
            cor += k
            coc += l
            if cor < 0 or cor >= len(s) or coc < 0 or coc >= len(s[0]):
                break
        if cor < 0 or cor >= len(s) or coc < 0 or coc >= len(s[0]):
            continue
        if s[cor][coc] == status:
            su += 1
    return su


def step(s):
    new = s.copy()
    for r in range(len(s)):
        for c in range(len(s[0])):
            if s[r][c] == '.':
                continue
            elif s[r][c] == 'L':
                su = sis(s, r, c, '#')
                if su == 0:
                    new[r] = new[r][:c] + '#' + new[r][c + 1:]
            elif s[r][c] == '#':
                su = sis(s, r, c, '#')
                if su >= 5:
                    new[r] = new[r][:c] + 'L' + new[r][c + 1:]
    return new


def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    last = lines.copy()
    s = step(lines)
    while last != s:
        last = s.copy()
        s  = step(s)
    total = 0
    for line in s:
        total += line.count('#')
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
