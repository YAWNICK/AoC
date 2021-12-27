import os

def compute(s: str):
    b = s.splitlines()
    moved = True
    step = 1
    rlen = len(b[0])
    clen = len(b)
    print(b)
    #for s in range(5):
    while moved:
        moved = False
        print("step", step)
        for ri in range(clen):
            left, right = b[ri][0], b[ri][-1]
            i = rlen-2
            while i >= 0:
            #for i in range(rlen-2,-1,-1):
                if b[ri][i] == '>' and b[ri][i+1] == '.':
                    b[ri] = b[ri][:i] + '.>' + b[ri][i+2:]
                    moved = True
                    i -= 1
                i -= 1
            if right == '>' and left == '.':
                b[ri] = '>' + b[ri][1:-1] + '.'
                moved = True
        for ci in range(rlen):
            top, bottom = b[0][ci], b[-1][ci]
            i = clen-2
            while i >= 0:
            #for i in range(clen-2,-1,-1):
                if b[i][ci] == 'v' and b[i+1][ci] == '.':
                    b[i] = b[i][:ci] + '.' + b[i][ci+1:]
                    b[i+1] = b[i+1][:ci] + 'v' + b[i+1][ci+1:]
                    moved = True
                    i -= 1
                i -= 1
            if bottom == 'v' and top == '.':
                b[clen-1] = b[clen-1][:ci]+'.'+b[clen-1][ci+1:]
                b[0] = b[0][:ci] + 'v' + b[0][ci+1:]
                moved = True
        step += 1
        #print(b)
    return step-1

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [58]
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
