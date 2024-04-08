import os

def compute(s: str):
    ## if single value:
    s = s.strip()
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
    
    while (red := list(map(lambda x: (x[0], x[1][0]), wf_label_res_same(WFS)))):
        for lbl, res in red:
            for wf in WFS.values():
                pass


                              


                              




    #items = list(map(lambda x: tuple(map(lambda y: int(y[2:]), x[1:-1].split(','))), items.splitlines()))
    #result = 0
    #for item in items:
    #    if valid(WFS, item):
    #        result += sum(item)
    print(result)
    return result

def wf_label_res_same(WFS):
    return list(filter(lambda item: item[1].count(item[1][0]) == len(item[1]), wf_label_res(WFS)))

def wf_label_res(WFS):
    return list(map(lambda item: (item[0], wf_results[item[1]]), WFS.items()))

def wf_results(wf):
    return tuple(cond[1] for cond in wf[1:]) + (wf[-1],)

def valid(WFS, item):
    label = 'in'
    while label not in 'AR':
        wf = WFS[label]
        nlabel = wf[-1]
        for cond in wf[:-1]:
            ind, cmp, th, res = cond
            if eval(f'{item[ind]}{cmp}{th}'):
                nlabel = res
                break
        label = nlabel
    return label == 'A'

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
