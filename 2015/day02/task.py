import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    lines = list(map(lambda x: x.split('x'),lines))
    lines = list(map(lambda x: list(map(int,x)), lines))
    res = 0
    for p in lines:
        #s1, s2, s3 = p[0]*p[1], p[1]*p[2], p[2]*p[0]
        #res += 2*s1+2*s2+2*s3+min([s1,s2,s3])
        s1, s2, s3 = 2*p[0]+2*p[1], 2*p[1]+2*p[2], 2*p[2]+2*p[0]
        res += min([s1,s2,s3]) + p[0]*p[1]*p[2]
    return res

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
