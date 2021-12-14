import os
from collections import defaultdict

def compute(s: str, rounds: int):
    lines = s.splitlines()
    s = lines[0]  # start string
    S = defaultdict(int)  # count pair occurrences
    for seq in zip(s, s[1:]):
        S[seq[0]+seq[1]] += 1
    G = {}  # map pair to the 2 new pairs it creates
    for rule in lines[2:]:
        seq, ins = rule.split(' -> ')
        G[seq] = (seq[0]+ins, ins+seq[1])
    for i in range(rounds):  # main loop
        for seq, cnt in S.copy().items():
            if S[seq] >= cnt:
                S[seq] -= cnt
            sub1, sub2 = G[seq]
            S[sub1] += cnt
            S[sub2] += cnt
    res = defaultdict(int)  # count letter occurrences
    for seq, cnt in S.items():
        res[seq[1]] += cnt  # for each pair only count the 2nd letter, bc they overlap
    res[s[0]] += 1  # don't forget the very first letter of the string
    return max(res.values()) - min(res.values())

###############################################################################

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [2188189693529]
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
    print("Part 1:", compute(inp, 10))
    print("Part 2:", compute(inp, 40))

if __name__ == "__main__":
    main()
