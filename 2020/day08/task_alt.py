import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    accu = 0
    ip = 0
    visited = set()
    while ip not in visited:
        ins, n = lines[ip].split(' ')
        visited.add(ip)
        if ins == 'acc':
            accu += int(n)
            ip += 1
        elif ins == 'jmp':
            ip += int(n)
        else:
            ip += 1

    return accu

def compute2(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    for i in range(len(lines)):
        accu = 0
        ip = 0
        visited = set()
        while ip not in visited and ip != 683:
            ins, n = lines[ip].split(' ')
            visited.add(ip)
            if ip == i and ins in ['nop', 'jmp']:
                ins = ['nop', 'jmp'][ins == 'nop']

            if ins == 'acc':
                accu += int(n)
                ip += 1
            elif ins == 'jmp':
                ip += int(n)
            else:
                ip += 1
        if ip == 683:
            return accu

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
    print("Part 1", compute(inp))
    print("Part 2", compute2(inp))

if __name__ == "__main__":
    main()
