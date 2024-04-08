import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    M = dict()
    M['broadcaster'] = None
    DM = dict()
    S = dict()
    I = dict()
    initial = None
    for line in lines:
        if line.startswith('broadcaster'):
            initial = line.split(' -> ')[1].split(', ')
            continue
        module, dst = line.split(' -> ')
        t, lbl = module[0], module[1:]
        M[lbl] = t
        DM[lbl] = dst.split(', ')
        if t == '%':
            S[lbl] = 0
    for lbl in M:
        if M[lbl] != '&':
            continue
        inputs = dict()
        for cand in DM:
            if lbl in DM[cand]:
                inputs[cand] = 0
        I[lbl] = inputs
    print('n of &s', len(I))
    print(initial)
    leninitial = len(initial)
    print('leninitial', leninitial)
    i = 0
    phi = 0
    plo = 0
    done = False
    for _ in range(10000):
    #while not done:
        Q = list(map(lambda x: (x, 0, 'broadcaster'), initial))
        plo += 1 + leninitial
        #print('button press')
        while Q:
            lbl, pulse, src = Q.pop(0)
            #print(src, pulse, lbl)
            if src in ['cs', 'rd', 'qs', 'mj'] and pulse == 0:
                print('  ', i+1, src)
            if lbl not in M:
                continue
            t = M[lbl]
            #print(t, lbl, pulse, src, M[src])
            #dst = DS[lbl]
            if t == '%':
                if pulse == 1:
                    continue
                S[lbl] = 0 if S[lbl] == 1 else 1
                for dm in DM[lbl]:
                    Q.append((dm, S[lbl], lbl))
                    phi += 1 if S[lbl] == 1 else 0
                    plo += 1 if S[lbl] == 0 else 0
            elif t == '&':
                I[lbl][src] = pulse
                p_out = 1
                if sum(I[lbl].values()) == len(I[lbl].values()):
                    p_out = 0
                for dm in DM[lbl]:
                    Q.append((dm, p_out, lbl))
                    phi += 1 if p_out == 1 else 0
                    plo += 1 if p_out == 0 else 0
            else:
                print('ERROR')
        
        i += 1
        #print(i, ''.join(map(lambda x: str(x[1]), sorted(S.items()))))
        #print(plo, phi)
        #if 1 in S.values():
        #    continue
        #if any([1 in I[item].values() for item in I]):
        #    continue
        #break
    #print('found loop after', i, 'steps')
    #print(plo, phi, phi*plo)
    print('pulses for rx', i)
    return 

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [32000000, 11687500]
    # testing begins here
    cnt = 1
    while os.path.exists(f"tests/{cnt}.txt"):
        print(f"TEST {cnt} ================")
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
