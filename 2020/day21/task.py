import os
import re
from functools import reduce

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    ings, algs = [], []  # contain the ingredients and allergens
    for food in lines:
        ing, alg = food.split(' (contains ')
        ings.append(set(ing.split(' ')))
        algs.append(alg[:-1].split(', '))
    allalgs = set()  # set of all allergens ever mentioned
    for food in algs:
        for alg in food:
            allalgs.add(alg)
    algapp = {}  # maps each allergen to the foods in which it occurs
    for alg in allalgs:
        isin = []
        for i, foodalgs in enumerate(algs):
            if alg in foodalgs:
                isin.append(i)
        algapp[alg] = isin
    algcands = {}  # maps each allergen to its ingredient candidates
    for alg, apps in algapp.items():
        cands = ings[apps[0]].copy()
        for foodind in apps[1:]:
            cands.intersection_update(ings[foodind])
        algcands[alg] = cands
    # look at this and figure part 2 out manually
    print("Part 2 (figure the rest out by yourself):")
    for alg in algcands.items():
        print(alg)
    # for part 1:
    # find all ingredients which contain an allergen
    algings = reduce(set.union, algcands.values())
    total = 0
    for food in ings:
        part = food.difference(algings)
        total += len(part)
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
    print("Part 1:", compute(inp))

if __name__ == "__main__":
    main()
