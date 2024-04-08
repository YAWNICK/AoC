import os


D = {('-',0,-1):(0,1)}

def next(s, py, px):
    if s == '-':
        return py, -px
    elif s == '|':
        return -py, px
    elif s == 'F' or s == 'J':
        return px, py
    elif s == '7' or 'L':
        return -px, -py
    else:
        print('ERROR....')

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    xlen, ylen = len(lines[0]), len(lines)
    xS, yS = None, None
    for j in range(ylen):
        for i in range(xlen):
            if lines[j][i] == 'S':
                xS = i
                yS = j
    yC, xC = yS, xS-1
    yP, xP = 0, 1
    #yC, xC = yS+1, xS
    #yP, xP = -1, 0
    #d = 1
    pathps = [(yS, xS)]
    while not (yC, xC) == (yS, xS):
        pathps.append((yC, xC))
        dy, dx = next(lines[yC][xC], yP, xP)
        yC, xC = yC+dy, xC+dx
        yP, xP = -dy, -dx
        #d += 1
    #print(d / 2)
    #my = max(map(lambda x: x[0], pathps))
    #print(my)
    yC, xC = yS, xS-1
    yP, xP = 0, 1
    #yC, xC = yS+1, xS
    #yP, xP = -1, 0
    inner = set()
    while not (yC, xC) == (yS, xS):
        s = lines[yC][xC]
        if s == '|' and yP==1 or s=='7' and yP==1 or s=='J' and xP==-1:
            yF, xF = yC, xC+1
            while (yF, xF) not in pathps:
                inner.add((yF, xF))
                xF += 1
        elif s=='|' and yP==-1 or s=='L' and yP==-1 or s=='F' and xP==1:
            yF, xF = yC, xC-1
            while (yF, xF) not in pathps:
                inner.add((yF, xF))
                yF -= 1
        elif s=='-' and xP==-1 or s=='J' and xP==-1 or s=='L' and yP==-1:
            yF, xF = yC+1, xC
            while (yF, xF) not in pathps:
                inner.add((yF, xF))
                yF += 1
        elif s=='-' and xP==1 or s=='F' and xP==1 or s=='7' and yP==1:
            yF, xF = yC-1, xC
            while (yF, xF) not in pathps:
                inner.add((yF, xF))
                yF -= 1
        
        #go to next
        dy, dx = next(s, yP, xP)
        yC, xC = yC+dy, xC+dx
        yP, xP = -dy, -dx
    res = len(inner)
    print(res)
    return res

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [10]
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
    #run_tests()
    inp = read_input("input.txt")
    print(compute(inp))

if __name__ == "__main__":
    main()
