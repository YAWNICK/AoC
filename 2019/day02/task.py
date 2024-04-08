

def compute(s: str):
    ## if single value:
    s = s.strip()
    ## if multiple values in multiple lines
    ## assuming no newline at the end of the input file
    #lines = s.splitlines()
    data = list(map(int, s.split(',')))
    data[1] = 12
    data[2] = 2
    i = 0
    while data[i] != 99:
        op = data[i]
        if op == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif op == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        i += 4
    return data[0]

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
