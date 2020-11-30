

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    ## assuming no newline at the end of the input file
    lines = s.splitlines()
    total = 0
    for line in lines:
        n = int(line)
        fuel_req = 0
        while True:
            if ((n // 3) - 2) < 0:
                break
            fuel_req += (n // 3) -2
            n = (n // 3) - 2
        total += fuel_req

    return total

def read_input() -> str:
    inp = ""
    with open("input.txt", 'r') as f:
        inp = f.read()
    return inp

def main():
    inp = read_input()
    print(compute(inp))

if __name__ == "__main__":
    main()
