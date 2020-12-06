import os

def cnt(s):
    p = 1
    q = {}
    for c in s:
        if c in q.keys():
            q[c] += 1
        else:
            q[c] = 1
        if c ==  '#':
            p += 1
    # part 1:
    # return len(q.keys())
    return list(q.values()).count(p)

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    #lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    lines = s.split('\n\n')
    cnts = 0
    groups = []
    for line in lines:
        line = line.replace('\n', '#')
        groups.append(cnt(line))


    return sum(groups)

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
