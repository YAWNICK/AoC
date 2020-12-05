import os
import re

def seatId(row, col):
    return row * 8 + col

def row(c):
    b = map(lambda x: '0' if x == 'F' else '1', c)
    return list(b)

def col(c):
    b = map(lambda x: '0' if x == 'L' else '1', c)
    return list(b)

def todec(b):
    r = 0
    for i in range(len(b)):
        r += int(b[i]) * (2**(len(b)-1-i))
    return r

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    seats = []
    for line in lines:
        r = row(line[:7])
        c = col(line[7:])
        seat = seatId(todec(r), todec(c))
        seats.append(seat)
    for r in range(1, 127):
        for c in range(8):
            s = seatId(r, c)
            if s not in seats:
                if seatId(r, c - 1) in seats and seatId(r, c + 1) in seats:
                    return s
    return None

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
