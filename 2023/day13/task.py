import os

def compute(s: str):
    ## if single value:
    s = s.strip()
    ## if multiple values in multiple lines
    #lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    fields = s.split('\n\n')
    res = 0
    for field in fields:
        f = field.splitlines()
        oval = find_value(f, 0)
        val = None
        for i in range(len(f)):
            for j in range(len(f[0])):
                fsmudge = f[:]
                nch = '.' if fsmudge[i][j] == '#' else '#'
                fsmudge[i] = fsmudge[i][:j] + nch + fsmudge[i][j+1:]
                val = find_value(fsmudge, oval)
                #if val == oval:
                #    val = None
                if val:
                    break
            if val:
                break
        '''
        if val is None:
            print(oval)
            i = 6
            j = 0
            fsm = f[:]
            fsm[i]=fsm[i][:j] + '#' + fsm[i][j+1:]
            for line in fsm:
                print(line)
            #ff = list(map(lambda z: ''.join(z), zip(*fsm))) 
            #ffi = list(map(lambda line: int(line.replace('.','0').replace('#','1'), 2), ff))
            #print(find_mirror(ffi))
            print(find_value(fsm, oval))
            for line in f:
                print(line)
        '''
        res += val
    print(res)
    return res

def find_value(f, oval):
    ff = list(map(lambda z: ''.join(z), zip(*f)))
    fi = list(map(lambda line: int(line.replace('.','0').replace('#','1'), 2), f))
    ffi = list(map(lambda line: int(line.replace('.','0').replace('#','1'), 2), ff))
    vals = []
    if off := find_mirror(fi):
        vals.append(100*off)
    if off := find_mirror(fi[::-1]):
        vals.append(100*(len(fi)-off))
    if off := find_mirror(ffi):
        vals.append(off)
    if off := find_mirror(ffi[::-1]):
        vals.append(len(ffi)-off)
    if oval in vals:
        vals.remove(oval)
    return None if vals == [] else vals[0]

def find_mirror(f):
    for i in range(len(f)-4):
        if f[i:i+4].count(f[i]) == 4:
            print('ERROR')
    stack = [f[0]]
    for i, n in enumerate(f[1:]):
        if n == stack[-1]:
            stack.pop()
        else:
            stack.append(n)
        if stack == []:
            return (i+2) // 2
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
