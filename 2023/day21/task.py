import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    yS, xS = 0, 0
    ylen = len(lines)
    xlen = len(lines[0])
    print(ylen, xlen)
    for y in range(ylen):
        for x in range(xlen):
            if lines[y][x] == 'S':
                yS = y
                xS = x
    data = lines
    #data = [line*5 for line in lines*5]
    #yS, xS = yS+131*2, xS+131*2
    pset = set()
    ppset = set()
    cset = {(yS, xS)}
    offset = set()
    mainset = set()
    for i in range(66+131):
        nset = set()
        for y, x in cset:
            for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                yn, xn = y + dy, x + dx
                if yn < 0 or yn >= ylen or xn < 0 or xn >= xlen:
                    continue
                if data[yn][xn] != '#':
                    nset.add((yn, xn))
        #print(len(nset), (yS, xS) in nset)
        cset = nset
        if i == 131+65:
            mainset = nset.copy()
        if i == 131+64:
            offset = nset.copy()
    #D = [[ch for ch in line] for line in data]
    #for y, x in cset:
    #    D[y][x] = 'O'
    #for row in D:
    #    print(''.join(row))
    
    print(len(mainset), (yS, xS) in mainset)
    print(len(offset), (yS, xS) in offset)
    return 

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
