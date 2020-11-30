

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    ## assuming no newline at the end of the input file
    #lines = s.splitlines()
    
    return 

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
