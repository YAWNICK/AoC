import os

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    #lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    wfs, items = s.split('\n\n')
    WFS = dict()
    CATS = {'x': 0, 'm': 1, 'a': 2, 's': 3}
    for wf in wfs.splitlines():
        label, wf = wf.split('{')
        wf = wf[:-1]
        wf = wf.split(',')
        wflist = []
        for item in wf:
            if not ':' in item:
                wflist.append(item)
                continue
            condition, res = item.split(':')
            if '<' in condition:
                cat, th = condition.split('<')
                wflist.append([CATS[cat], '<', int(th), res)
            elif '>' in condition:
                cat, th = condition.split('>')
                wflist.append([CATS[cat], '>', int(th), res])
            else:
                print('ERROR')
        WFS[label] = wflist

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
    print(compute(inp))

if __name__ == "__main__":
    main()
