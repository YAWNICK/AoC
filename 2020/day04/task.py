import os
import re

# Not pretty.
# useful stuff to take a look at: all(), any(), map()
# and: more list comprehensions
# and also: memorize some re


def compute(s: str):
    ## if single value:
    s = s.strip()
    ## if multiple values in multiple lines
    #lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    total = 0
    f = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    ss = s.split('\n\n')
    for p in ss:
        p = p.replace('\n', ' ')
        fields = [k.split(':') for k in p.split(' ')]
        g = f.copy()
        for field in fields:
            if field[0] in f:
                fi = field[0]
                v = False
                fl = field[1]
                if fi == 'byr':
                    if int(fl) >= 1920 and int(fl) <= 2002:
                        v = True
                elif fi == 'iyr':
                    if int(fl) >= 2010 and int(fl) <= 2020:
                        v = True
                elif fi == 'eyr':
                    if int(fl) >= 2020 and int(fl) <= 2030:
                        v = True
                elif fi == 'hgt':
                    if fl[-2] == 'c':
                        h = int(fl[:-2])
                        if h >= 150 and h <= 193:
                            v = True
                    elif fl[-2] == 'i':
                        h = int(fl[:-2])
                        if h >= 59 and h <= 76:
                            v = True
                elif fi == 'hcl':
                    if fl[0] == '#':
                        o = True
                        for l in fl[1:]:
                            if l not in '0123456789abcdef':
                                o = False
                        v = o
                elif fi == 'ecl':
                    if fl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        v = True
                elif fi == 'pid':
                    if re.search('^[0-9]{9}$', fl):
                        v = True
                if v == True:
                    g.remove(field[0])
        if len(g) == 0:
            total += 1
            

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
