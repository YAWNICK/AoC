import os
import re

class Expr:
    
    def __init__(self, s):
        self.ops = []
        self.vals = []
        # recursively create Expr objects and fill ops and vals
        csub = ''
        d = 0  # parenthesis depth
        for c in s:
            if d == 0:
                if c in '+*':
                    self.ops.append(c)
                elif c in '0123456789':
                    self.vals.append(c)
                elif c == '(':
                    d += 1
            elif d >= 1:
                if c == '(':
                    d += 1
                elif c == ')':
                    d -= 1
                csub = csub + c
                if d == 0:
                    self.vals.append(Expr(csub[:-1]))  # leave out the closing ')'
                    csub = ''

    def get_or_eval(self, val_index):
        item = self.vals[val_index]
        if type(item) == self.__class__:
            item = item.eval()
        return int(item)

    def eval(self):
        # do most of the work for part 2 by evaluating addition first
        # uncomment to solve just for part 1
        ops = []
        vals = []
        curr = self.get_or_eval(0)
        for i in range(len(self.ops)):
            if self.ops[i] == '*':
                vals.append(curr)
                ops.append('*')
                curr = self.get_or_eval(i + 1)
            else:
                curr += self.get_or_eval(i + 1)
        vals.append(curr)

        self.ops = ops
        self.vals = vals

        # regular evaluation with no precedence

        r = self.get_or_eval(0)
        for i in range(len(ops)):
            op = ops[i]
            val = self.get_or_eval(i + 1)
            if op == '*':
                r *= val
            else:
                r += val
        return r


def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    total = 0
    for line in lines:
        total += Expr(line).eval()
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
    print(compute(inp))

if __name__ == "__main__":
    main()
