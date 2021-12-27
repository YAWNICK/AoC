import os
from collections import defaultdict

G = defaultdict(list)
res1 = 0

def compute(s: str, part: int):
    global res1
    global G
    G = defaultdict(list)
    res1 = 0
    lines = s.splitlines()
    for line in lines:
        a, b = line.split('-')
        G[a].append(b)
        G[b].append(a)
    if part == 1:
        find1('start', set(), [])
    else:
        find('start', set(), False, [])
    return res1

def find1(node, visited, path):
    global res1
    global G
    path.append(node)
    if node == 'end':
        res1 += 1
        return
    if node.islower():
        visited.add(node)
    for nb in G[node]:
        if nb not in visited:
            find1(nb, visited.copy(), path.copy())

def find(node, visited, hasdouble, path):
    global res1
    global G
    path.append(node)
    if node == 'end':
        p = list(filter(str.islower, path))
        if hasdouble and len(p) == len(set(p)):
            res1 -= 1
        res1 += 1
        return
    visitedwo = visited.copy()
    if node.islower():
        visited.add(node)
    for nb in G[node]:
        if nb not in visited:
            find(nb, visited.copy(), hasdouble, path.copy())
            if node.islower() and not hasdouble and node != 'start':
                find(nb, visitedwo.copy(), True, path.copy())


def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [36]
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
