import os

def get_score(c1, c2):
    w = c1 if c1 else c2
    fac = [i + 1 for i in range(len(w) - 1, -1, -1)]
    return sum(map(lambda x: x[0] * x[1], zip(w, fac)))

def compute(s: str):
    ps = s.split('\n\n')
    c1, c2 = list(map(lambda x: list(map(int, x.splitlines()[1:])), ps))
    while c1 and c2:
        pc1 = c1.pop(0)
        pc2 = c2.pop(0)
        if pc1 > pc2:
            c1 += [pc1, pc2]
        else:  # pc2 > pc1
            c2 += [pc2, pc1]
    return get_score(c1, c2)

def compute2(s: str):
    ps = s.split('\n\n')
    c1, c2 = list(map(lambda x: list(map(int, x.splitlines()[1:])), ps))
    c1, c2, _ = rec(c1, c2, [])
    return get_score(c1, c2)

def rec(c1, c2, mem):
    while c1 and c2:
        if [c1, c2] in mem:
            return c1, c2, 'p1'
        mem.append([c1.copy(), c2.copy()])
        pc1 = c1.pop(0)
        pc2 = c2.pop(0)
        w = 2  # assume p2 wins this round and change to p1 if not
        if len(c1) >= pc1 and len(c2) >= pc2:  # recursive game
            _, _, winner = rec(c1[:pc1], c2[:pc2], [])
            if winner == 'p1':
                w = 1
        else:  # standard game
            if pc1 > pc2:
                w = 1
        # update cards
        if w == 1:
            c1 += [pc1, pc2]
        else:
            c2 += [pc2, pc1]
    # if one has all cards
    if c1 == []:
        return c1, c2, 'p2'
    else:  # c2 == []
        return c1, c2, 'p1'

# setup

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
    print("Part 2:", compute2(inp))

if __name__ == "__main__":
    main()
