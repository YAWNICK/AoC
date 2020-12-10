import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    lines = list(map(int, lines))
    a = [0]
    d1 = 0
    d3 = 0
    d2 = 0
    while lines != []:
        c = a[-1]
        n = min(lines)
        a.append(n)
        lines.remove(n)
        if n - c == 1:
            d1 += 1
        elif n - c == 2:
            d2 += 1
        elif n - c == 3:
            d3 += 1
    d3 += 1
    #return (d1, d2, d3)
    return d1 * d3

# part 2

def packet(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return packet(n-1) + packet(n-2) + packet(n-3)

def compute2(s:str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    lines = list(map(int, lines))
    total = 1
    lines.sort()
    last = 0
    curr = 0
    for i in range(len(lines)):
        if lines[i] - last == 1:
            curr += 1
        else:
            if curr != 0:
                total = total * packet(curr)
                curr = 0
        last = lines[i]
    if curr != 0:
        total = total * packet(curr)
    return total

# setup

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [8, 19208]
    # testing begins here
    cnt = 1
    while os.path.exists(f"tests/{cnt}.txt"):
        if (r := compute2(read_input(f"tests/{cnt}.txt"))) == solutions[cnt - 1]:
            print(f"Test {cnt} successful!")
        else:
            print(f"Test {cnt} failed!")
            print(f"  result: {r}")
            print(f"  was supposed to be {solutions[cnt - 1]}")
        cnt += 1
    print("---TESTS END---")

def main():
    run_tests()
    inp = read_input("input.txt")
    print(compute(inp))
    print(compute2(inp))

if __name__ == "__main__":
    main()
