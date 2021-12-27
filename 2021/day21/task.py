import os


Dist = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

def play(ps, ss, turn, cnt, ws):
    nt = 1 if turn == 0 else 0
    if ss[nt] >= 21:
        ws[nt] += cnt
        return ws
    for d, n in Dist.items():
        psc = ps.copy()
        psc[turn] = (psc[turn] + d) % 10
        ssc = ss.copy()
        ssc[turn] += psc[turn]+1
        ws = play(psc, ssc, nt, cnt*n, ws)
    return ws

def compute2():
    ws = play([0,9], [0,0], 0, 1, [0,0])
    return max(ws)

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    #lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    dist = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
    p1s = 1
    p2s = 10
    die = 0
    board = [0]*10
    p1score = 0
    p2score = 0
    turn = 1
    ps = [0,9]
    scores= [0,0]
    drs = 0
    while max(scores) < 1000:
        d = 0
        for i in range(3):
            drs += 1
            die += 1
            if die > 100:
                die -= 100
            d += die
        #d = ((die+1) % 100)+((die+2)%100)+((die+3)%100)
        #die+= 3
        #die %= 100
        ps[turn-1] += d
        ps[turn-1] %= 10
        #if ps[turn-1] >10:
        #    ps[turn-1] -= 10
        scores[turn-1] += ps[turn-1]+1
        turn = 2 if turn == 1 else 1
    print(scores)
    print(ps)
    print(drs)
    ls = scores[0] if scores[0] < 1000 else scores[1]
    print(ls*drs)
    return 

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
    print(compute2())

if __name__ == "__main__":
    main()
