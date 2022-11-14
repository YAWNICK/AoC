import os
import re
import numpy as np

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    pat = '(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)'
    lines = [(s,int(x1),int(y1),int(x2),int(y2)) for s,x1,y1,x2,y2 in map(lambda x: re.match(pat, x).groups(), lines)]
    G = np.zeros((1000,1000))
    for line in lines:
        s, x1, y1,x2,y2 = line
        for x in range(min(x1,x2), max(x1,x2)+1):
            for y in range(min(y1,y2), max(y1,y2)+1):
                curr = G[x,y]
                # if s == 'turn on' or s == 'toggle' and curr == 0:
                #     G[x,y] = 1
                # else:
                #     G[x,y] = 0
                if s == 'turn on':
                    G[x,y] = curr + 1
                elif s == 'toggle':
                    G[x,y] = curr + 2
                else:
                    G[x,y] = max(curr-1,0)
    
    return G.sum()

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
