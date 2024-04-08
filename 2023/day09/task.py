import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    res = 0
    for line in lines:
        ns = list(map(int, line.split()))
        lasts = [ns[-1]]
        firsts = [ns[0]]
        row = ns
        while row.count(0) != len(row):
            row = [x-y for x,y in zip(row[1:], row[:-1])]
            lasts.append(row[-1])
            firsts.append(row[0])
        lasts = lasts[::-1]
        firsts = firsts[::-1]
        ip = [0]
        for i in range(1, len(firsts)):
            #ip.append(ip[i-1]+lasts[i])
            ip.append(firsts[i]-ip[i-1])
        res += ip[-1]
    return res

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [114]
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
