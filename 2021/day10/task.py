import os
from functools import reduce

def compute(s: str, part: int):
    lines = s.splitlines()
    res = 0  # result for part 1
    skip = []  # indices to skip for part 2
    for i, line in enumerate(lines):
        stack = ''
        for c in line:
            if c in '([{<':
                stack += c
            else:
                if stack[-1] == {')':'(',']':'[','}':'{','>':'<'}[c]:
                    stack = stack[:-1]
                else:
                    res += [3, 57, 1197, 25137][')]}>'.index(c)]
                    skip.append(i)
                    break
    if part == 1:
        return res
    # Part 2
    rs = []  # scores
    for line in [line for i, line in enumerate(lines) if i not in skip]:
        stack = ''
        for c in line:
            if c in '([{<':
                stack += c
            else:
                stack = stack[:-1]
        seq = stack[::-1]
        r = reduce(lambda x, c: x * 5 + ' ([{<'.index(c), seq, 0)
        rs.append(r)
    rs = sorted(rs)
    return rs[(len(rs) // 2)]

###############################################################################

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [288957]
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
    print("Part 1:", compute(inp, 1))
    print("Part 2:", compute(inp, 2))

if __name__ == "__main__":
    main()
