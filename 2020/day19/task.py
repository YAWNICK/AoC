import os

# this solution takes advantage of lots of ways in which the input is a special
# case of the general problem.
# - most rules indirectly contain an 'a' or 'b'
# - only character strings of length 8 match rules 42 and 31
# - an 8 character string never seems to match both rules 42 and 31

def compute(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    rules = lines[:132]
    words = lines[133:]
    rs = {}
    for rule in rules:
        n, r = rule.split(': ')
        cont = r.split(' | ')
        rs[n] = cont
    total = 0
    for word in words:
        parts = len(word) // 8
        fit = []
        for i in range(parts):
            part = word[i*8:(i*8)+8]
            f = []
            if fits(part, rs, '42'):
                fit.append('42')
            if fits(part, rs, '31'):
                fit.append('31')
        # part 2:
        if '31' not in fit or '42' not in fit:
            continue
        if '42' not in fit[fit.index('31'):] and fit.count('42') > fit.count('31'):
            total += 1
        # part 1
        #if fit == ['42', '42', '31']:
        #    total += 1
    return total

def fits(word, rs, rn):
    if word == '':
        return False
    if rn == '105':
        if len(word) == 1:
            return True
        else:
            return False
    elif rn == '7':
        if word == 'a':
            return True
        else:
            return False
    elif rn == '13':
        if word == 'b':
            return True
        else:
            return False
    elif rn == '27':
        if len(word) == 2:
            return True
        else:
            return False
    r = rs[rn]
    valid = 0
    for rule in r:
        rl, rr = rule.split(' ')
        if rl in ['13', '7']:
            if fits(word[:1], rs, rl) and fits(word[1:], rs, rr):
                valid += 1
        elif rr in ['13', '7']:
            if fits(word[:-1], rs, rl) and fits(word[-1:], rs, rr):
                valid += 1
    if valid > 0:
        return True
    else:
        return False

# setup

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [42]
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
