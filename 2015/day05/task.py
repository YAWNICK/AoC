import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    cnt = 0
    for line in lines:
        # if len(list(filter(lambda x: x in 'aeiou', line))) < 3:
        #     continue
        # if len(list(filter(lambda x: x[0]==x[1], zip(line[:-1], line[1:])))) < 1:
        #     continue
        # if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
        #     continue
        pairs = list(zip(line[:-1], line[1:]))
        i = 0
        while i < len(pairs)-1:
            if pairs[i] == pairs[i+1]:
                pairs.pop(i)
            i += 1
        if len(pairs) == len(set(pairs)):
            continue
        if len(list(filter(lambda x: x[0]==x[2], zip(line[:-2], line[1:-1], line[2:])))) < 1:
            continue
        cnt += 1
    return cnt

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
