import os


def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    dirs = lines[0]
    dirlen = (len(dirs))
    lines = lines[2:]
    G = dict()
    for line in lines:
        nid, nbs = line.split(' = ')
        nbs = nbs[1:-1].split(', ')
        G[nid] = nbs
    print('XVZ' in G.keys())
    lnodes = list(G.keys())
    sn = list(filter(lambda node: node.endswith('A'), lnodes))
    lsn = len(sn)
    print(sn)
    for node in sn:
        print(node, go(G, dirs, node, lambda n: n.endswith('Z')))
        print('-----') 
    print('--------------')
    print('ZZZ', go(G, dirs, 'ZZZ', lambda n: n.endswith('Z')))
    print('XVZ', go(G, dirs, 'XVZ', lambda n: n.endswith('Z')))
    print('QQZ', go(G, dirs, 'QQZ', lambda n: n.endswith('Z')))
    print('VGZ', go(G, dirs, 'VGZ', lambda n: n.endswith('Z')))
    print('PPZ', go(G, dirs, 'PPZ', lambda n: n.endswith('Z')))
    print('QFZ', go(G, dirs, 'QFZ', lambda n: n.endswith('Z')))
    return 

def go(G, dirs, start, endcrit):
    curr = start
    nsteps = 0
    dirlen = len(dirs)
    while not(endcrit(curr) and nsteps > 0):
        step = dirs[nsteps % dirlen]
        curr = G[curr][0] if step =='L' else G[curr][1]
        nsteps += 1
    return nsteps, curr



def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [6]
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
