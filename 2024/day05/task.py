import os
from parsing import parse
from collections import defaultdict

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    #lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    data = parse(s, '\n\n2\n1|1i\n1,1i')
    rules, updates = data
    left = defaultdict(set)
    right = defaultdict(set)
    for l, r in rules:
        left[r].add(l)
        right[l].add(r)
    res = 0
    for update in updates:
        valid = True
        for i, x in enumerate(update):
            l, r = set(update[:i]), set(update[i+1:])
            if w := l.intersection(right[x]):# or r.intersection(left[x]):
                #res += getn(update[:], w, left, right)
                valid = False
                break
        #if valid:
        #    res += update[len(update) // 2]
        if not valid:
            res += getn(update, left, right)
    return res

def getn(update, left, right):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[j] in left[update[i]]:
                update[i], update[j] = update[j], update[i]

    return update[len(update) // 2]


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
