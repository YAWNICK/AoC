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

def rec(lines, cache, n, ma):
    if cache[n] != None:
        return cache[n]
    s = 0
    for i in range(3):
        if n + i + 1 in lines:
            s += rec(lines, cache, n + i + 1, ma)
    cache[n] = s
    return s

def compute3(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    lines = list(map(int, lines))
    end = max(lines) + 3
    lines.append(end)
    cache = {}
    for i in lines:
        cache[i] = None
    cache[end] = 1
    cache[0] = None
    return rec(lines, cache, 0, end)

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
        if (r := compute3(read_input(f"tests/{cnt}.txt"))) == solutions[cnt - 1]:
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
    print(compute3(inp))

if __name__ == "__main__":
    main()
