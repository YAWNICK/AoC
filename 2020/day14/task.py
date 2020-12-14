import os
import re

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    mem = {}
    mask = ''
    for line in lines:
        if line[:4] == 'mask':
            mask = line.split()[-1]
        else:
            addr, val = re.findall(r"[0-9]+", line)
            v = bin(int(val))[2:]
            while len(v) < len(mask):  # prepend with zeros
                v = '0' + v
            for i, c in enumerate(mask):
                if c == 'X':
                    continue
                elif c == '0' and v[i] == '1':
                    v = v[:i] + '0' + v[i+1:]
                elif c == '1' and v[i] == '0':
                    v = v[:i] + '1' + v[i+1:]
            mem[addr] = int(v, 2)
    return sum(mem.values())

def compute2(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    mem = {}
    mask = ''
    for line in lines:
        if line[:4] == 'mask':
            mask = line.split()[-1]
        else:
            addr, val = re.findall(r"[0-9]+", line)
            addrs = ['']
            a = bin(int(addr))[2:]
            while len(a) < len(mask):  # prepend with zeros
                a = '0' + a
            for i, c in enumerate(mask):
                new = []  # new addresses due to floating bits
                for j, ad in enumerate(addrs):
                    if c == 'X':
                        new.append(ad + '0')
                        addrs[j] = ad + '1'
                    elif c == '0':
                        addrs[j] = ad + a[i]
                    elif c == '1':
                        addrs[j] = ad + '1'
                addrs += new
            for ad in addrs:
                mem[ad] = int(val)
    return sum(mem.values())

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
