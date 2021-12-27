import os

Digits = range(1,10)

def eval(cmds, *ws):
    ws = list(ws)
    print(ws)
    vs = {'w':0,'x':0,'y':0,'z':0}
    for cmd in cmds:
        #print(cmd)
        instr, *args = cmd.split()
        if instr == 'inp':
            print("new z:", vs['z'])
            vs[args[0]] = ws.pop(0)
        elif instr == 'add':
            a1, a2 = args
            vs[a1] += int(a2) if not a2.islower() else vs[a2]
        elif instr == 'mul':
            a1, a2 = args
            vs[a1] *= int(a2) if not a2.islower() else vs[a2]
        elif instr == 'mod':
            a1, a2 = args
            vs[a1] %= int(a2) if not a2.islower() else vs[a2]
        elif instr == 'div':
            a1, a2 = args
            if vs[a1] < 0:
                print("Div with negative number !!!")
            vs[a1] //= int(a2) if not a2.islower() else vs[a2]
        elif instr == 'eql':
            a1, a2 = args
            a2 = int(a2) if not a2.islower() else vs[a2]
            vs[a1] = 1 if vs[a1] == a2 else 0
        #print(vs)
    return vs['z']

def version0(z, w):
    return z + w + 7

def version1(z, w, p1):
    z *= 26
    z += w + p1
    return z

def version2(z, w, p1, p2):
    x = (z % 26) - p1
    z //= 26
    if w != x:
        z *= 26
        z += w + p2
    return z

def v0_nzs(zs,p1):
    nzs = set()
    for z in zs:
        for d in Digits:
            nzs.add(z-p1-d)
    return nzs
    #return set(filter(lambda x: x >= 0, nzs))

def v1_nzs(zs,p1):
    nzs = set()
    for z in zs:
        cands = set()
        for d in Digits:
            cands.add(z-p1-d)
        cands = set(filter(lambda x: x % 26 == 0, cands))
        for cand in cands:
            nzs.add(cand // 26)
    return nzs
    #return set(filter(lambda x: x >= 0, nzs))

def v2_nzs(zs,p1,p2):
    nzs = set()
    for z in zs:
        # w == x
        for i in range(p1+1,p1+9+1):
            nzs.add(z*26+i)
        # w != x
        cands = set()
        for d in Digits:
            cands.add(z-p2-d)
        cands = set(filter(lambda x: x % 26 == 0, cands))
        #cands = set(map(lambda x: x // 26, cands))
        for cand in cands:
            for i in range(26):
                nzs.add(cand+i)
    return nzs
    #return set(filter(lambda x: x >= 0, nzs))

zs = []
num_valid_nums = 0

def valid_nums(i, z, num):
    global zs
    global num_valid_nums
    for w in range(1,10):
        valid = False
        if i == 1:
            if (nz := version0(z,w)) in zs[1]:
                valid = True
        elif i == 2:
            if (nz := version1(z,w,8)) in zs[2]:
                valid = True
        elif i == 3:
            if (nz := version1(z,w,2)) in zs[3]:
                valid = True
        elif i == 4:
            if (nz := version1(z,w,11)) in zs[4]:
                valid = True
        elif i == 5:
            if (nz := version2(z,w,3,6)) in zs[5]:
                valid = True
        elif i == 6:
            if (nz := version1(z,w,12)) in zs[6]:
                valid = True
        elif i == 7:
            if (nz := version1(z,w,14)) in zs[7]:
                valid = True
        elif i == 8:
            if (nz := version2(z,w,16,13)) in zs[8]:
                valid = True
        elif i == 9:
            if (nz := version1(z,w,15)) in zs[9]:
                valid = True
        elif i == 10:
            if (nz := version2(z,w,8,10)) in zs[10]:
                valid = True
        elif i == 11:
            if (nz := version2(z,w,12,6)) in zs[11]:
                valid = True
        elif i == 12:
            if (nz := version2(z,w,7,10)) in zs[12]:
                valid = True
        elif i == 13:
            if (nz := version2(z,w,6,8)) in zs[13]:
                valid = True
        elif i == 14:
            if (nz := version2(z,w,11,5)) == 0:
                print("Found sol.:",num+[w])
                num_valid_nums += 1
                return
        if num_valid_nums > 0:
            return
        if not valid:
            continue
        nnum = num[:]+[w]
        valid_nums(i+1,nz,nnum)


def compute(s: str):
    global zs
    global num_valid_nums
    #lines = s.splitlines()
    #ws = [9,7,9,9,9,5,9,7,9,9,3,4,9,5]
    #res = eval(lines,*ws)
    #print("final z:", res)

    # Main Part
    zs = [set() for i in range(14)]
    # digit 14
    zs[13] = v2_nzs(set([0]),11,5)
    print("14:",len(zs[13]),"zs with max",max(zs[13]))
    # digit 13
    zs[12] = v2_nzs(zs[13],6,8)
    print("13:",len(zs[12]),"zs with max",max(zs[12]))
    # digit 12
    zs[11] = v2_nzs(zs[12],7,10)
    print("12:",len(zs[11]),"zs with max",max(zs[11]))
    # digit 11
    zs[10] = v2_nzs(zs[11],12,6)
    print("11:",len(zs[10]),"zs with max",max(zs[10]))
    # digit 10
    zs[9] = v2_nzs(zs[10],8,10)
    print("10:",len(zs[9]),"zs with max",max(zs[9]))
    # digit 9
    zs[8] = v1_nzs(zs[9],15)
    print("09:",len(zs[8]),"zs with max",max(zs[8]))
    # digit 8
    zs[7] = v2_nzs(zs[8],16,13)
    print("08:",len(zs[7]),"zs with max",max(zs[7]))
    # difit 7
    zs[6] = v1_nzs(zs[7],14)
    print("07:",len(zs[6]),"zs with max",max(zs[6]))
    # difit 6
    zs[5] = v1_nzs(zs[6],12)
    print("06:",len(zs[5]),"zs with max",max(zs[5]))
    # difit 5
    zs[4] = v2_nzs(zs[5],3,6)
    print("05:",len(zs[4]),"zs with max",max(zs[4]))
    # difit 4
    zs[3] = v1_nzs(zs[4],11)
    print("04:",len(zs[3]),"zs with max",max(zs[3]))
    # difit 3
    zs[2] = v1_nzs(zs[3],2)
    print("03:",len(zs[2]),"zs with max",max(zs[2]))
    # difit 2
    zs[1] = v1_nzs(zs[2],8)
    print("02:",len(zs[1]),"zs with max",max(zs[1]))
    # difit 1
    zs[0] = v0_nzs(zs[1],7)
    print("01:",len(zs[0]),"zs with max",max(zs[0]))
    #print(zs[0])
    
    valid_nums(1,0,[])
    print("# valid nums:", num_valid_nums)
    return
    ### construct the number
    z = 0
    # digit 1
    w1 = 9
    while (nz := version0(z, w1)) not in zs[1]:
        w1 -= 1
    z = nz
    print("w1:",w1,"z:",z)
    # digit 2
    w2 = 9
    while (nz := version1(z,w2,8)) not in zs[2]:
        w2 -= 1
    z = nz
    print("w2:",w2,"z:",z)
    # digit 3
    w3 = 9
    while (nz := version1(z,w3,2)) not in zs[3]:
        w3 -= 1
    z = nz
    print("w3:",w3,"z:",z)
    # digit 4
    w4 = 9
    while (nz := version1(z,w4,11)) not in zs[4]:
        w4 -= 1
    z = nz
    print("w4:",w4,"z:",z)
    # digit 5
    w5 = 9
    while (nz := version2(z,w5,3,6)) not in zs[5]:
        w5 -= 1
    z = nz
    print("w5:",w5,"z:",z)
    # digit 6
    w6 = 9
    while (nz := version1(z,w6,12)) not in zs[6]:
        w6 -= 1
    z = nz
    print("w6:",w6,"z:",z)
    # digit 7
    w7 = 9
    while (nz := version1(z,w7,14)) not in zs[7]:
        w7 -= 1
    z = nz
    print("w7:",w7,"z:",z)
    # digit 8
    w8 = 9
    while (nz := version2(z,w8,16,13)) not in zs[8]:
        w8 -= 1
    z = nz
    print("w8:",w8,"z:",z)
    # digit 9
    w9 = 9
    while (nz := version1(z,w9,15)) not in zs[9]:
        w9 -= 1
    z = nz
    print("w9:",w9,"z:",z)
    # digit 10
    w10 = 9
    while (nz := version2(z,w10,8,10)) not in zs[10]:
        w10 -= 1
    z = nz
    print("w10:",w10,"z:",z)
    # digit 11
    w11 = 9
    while (nz := version2(z,w11,12,6)) not in zs[11]:
        w11 -= 1
    z = nz
    print("w11:",w11,"z:",z)
    # digit 12
    w12 = 9
    while (nz := version2(z,w12,7,10)) not in zs[12]:
        w12 -= 1
    z = nz
    print("w12:",w12,"z:",z)
    # digit 13
    w13 = 9
    while (nz := version2(z,w13,6,8)) not in zs[13]:
        w13 -= 1
    z = nz
    print("w13:",w13,"z:",z)
    # digit 14
    w14 = 9
    while (nz := version2(z,w14,11,5)) != 0:
        w14 -= 1
    z = nz
    print("w14:",w14,"z:",z)
    

    '''
    digits = range(1,10)
    zs = [set() for i in range(14)]
    m = 25
    # digit 14
    m14 = 0
    for z in range(m+1):
        for w in digits:
            if version2(z, w, 11, 5) == 0:
                zs[13].add(z)
                m14 = z
    print(len(zs[13]), "zs with max", m14)
    # digit 13
    m13 = 0
    calc13 = set()
    for z in range(m14*26+25+1):
        for w in digits:
            nz = version2(z,w,6,8)
            if nz not in calc13:
                if nz not in zs[13]:
                    continue
            zs[13].discard(nz)
            calc13.add(nz)
            zs[12].add(z)
            m13 = z
    zs[13] = calc13
    print(len(zs[12]), "zs with max", m13)
    # digit 12
    m12 = 0
    for z in range(m13*26+25+1):
        for w in digits:
            if version2(z, w, 7, 10) in zs[12]:
                zs[11].add(z)
                m12 = z
    print(len(zs[11]), "zs with max", m12)
    m11 = 0
    for z in range(m12*26+25+1):
        for w in digits:
            if version2(z, w, 12, 6) in zs[11]:
                zs[10].add(z)
                m11 = z
    print(len(zs[10]), "zs with max", m11)



    return 
    '''

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
