import os

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    dim = 4
    cycles = 6
    alive = []
    for x, line in enumerate(lines):
        for y, cell in enumerate(line):
            if cell == '#':
                pos = [x, y] + [0]*(dim - 2)
                alive.append(tuple(pos))
    ns = neighbour_coords(dim)
    for i in range(cycles):
        alive = step(alive, dim, ns)
    return len(alive)

def neighbour_coords(dim):
    ns = []
    for n in range(3**dim):    
        co = []
        for i in range(dim):
            co.append((n % 3) - 1)
            n = n // 3
        ns.append(co)
    return ns

def step(alive, dim, ns):
    nalive = {}  # <[int], int> // <coord, #neighbours>  
    for cell in alive:
        for nb in ns:
            if nb == [0]*dim:
                continue
            co = tuple(map(sum, zip(cell, nb)))
            nalive.setdefault(co, 0)
            nalive[co] += 1
    new = []
    for cell, cnt in nalive.items():
        if cell in alive and cnt == 2 or cnt == 3:
            new.append(cell)
    return new

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [848]
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
    print(compute(inp))

if __name__ == "__main__":
    main()
