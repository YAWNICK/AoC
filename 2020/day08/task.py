import os
import re

class HGC:

    def __init__(self, code):
        self.accu = 0
        self.ip = 0
        self.code = code
        self.visited = []

    def acc(self, n):
        self.accu += n

    def jmp(self, n):
        self.ip += n

    def runline(self):
        line = self.code[self.ip]
        i, n = line.split(' ')
        self.visited.append(self.ip)
        if i == 'acc':
            self.acc(int(n))
            self.ip += 1
        elif i == 'jmp':
            self.jmp(int(n))
        else:
            self.ip += 1

    def run(self):
        while self.ip != 683 and self.ip not in self.visited:
            self.runline()
        return self.accu

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    cands = []
    for i, line in enumerate(lines):
        if line.split(' ')[0] != 'acc':
            cands.append(i)
    for ip in cands:
        c = lines.copy()
        ins = c[ip].split(' ')[0]
        if ins == 'jmp':
            c[ip] = 'nop' + c[ip][3:]
        elif ins == 'nop':
            c[ip] = 'jmp' + c[ip][3:]
        hgc = HGC(c)
        accu = hgc.run()
        if hgc.ip == 683:
            return accu

    return "ERROR"

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
