import os
import re

# my tests changed the global variables and I didnt reset them in compute...
# also: regexes probably make stuff easier!! 

parents = {}
total = []
colors = {}

def gettotal(name):
    if name not in parents.keys():
        return 
    for p in parents[name]:
        if p[1] in total:
            continue
        total.append(p[1])
        gettotal(p[1])
    return

def contains(name):
    if colors[name] == []:
        return 0
    s = 0
    for c in colors[name]:
        s += c[0] + c[0] * contains(c[1])
    return s

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    colors.clear()
    parents.clear()
    total.clear()
    for line in lines:
        name, cont = line.split(' bags contain ')
        colors[name] = []
        if cont == "no other bags.":
            continue
        c = cont.split(', ')
        c[-1] = c[-1][:-1]
        for spec in c:
            n = int(spec[0])
            na = spec[2:-5] if n > 1 else spec[2:-4]
            colors[name].append((n, na))
            if na not in parents.keys():
                parents[na] = []
            parents[na].append((n, name))
    #part 1
    #return len(total)
    return contains('shiny gold')

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [32]
    # testing begins here
    cnt = 1
    while os.path.exists(f"tests/{cnt}.txt"):
        if compute(read_input(f"tests/{cnt}.txt")) == solutions[cnt - 1]:
            print(f"Test {cnt} successful!")
            print(f"  solution: {solutions[cnt - 1]}")
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
