import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    #lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    data = [(61, 430), (67, 1036), (75, 1307), (71, 1160)]
    #data = [(7, 9), (15, 40), (30, 200)]
    ways = []
    for time, record in data:
        n = 0
        for hold in range(time):
            res = hold*(time-hold)
            if res > record:
                n += 1
        ways.append(n)
    print(ways)
    time = 61677571
    record = 430103613071160
    n = 0
    for hold in range(time):
        res = hold*(time-hold)
        if res > record:
            n += 1
    return n
    return ways[0]*ways[1]*ways[2]*ways[3]

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
