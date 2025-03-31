import os
import networkx as nx

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    G = nx.Graph()
    for line in lines:
        node, nbs = line.split(': ')
        nbs = nbs.split()
        G.add_node(node)
        G.add_nodes_from(nbs)
        for nb in nbs:
            G.add_edge(node, nb)
    bc = nx.edge_betweenness_centrality(G)
    bc = sorted(list(bc.items()), key=lambda x: x[1], reverse=True)[:10]
    print(bc)
    G.remove_edge(*bc[0][0])
    G.remove_edge(*bc[1][0])
    G.remove_edge(*bc[2][0])
    cc = list(nx.connected_components(G))
    #print(cc)
    print(len(cc))
    print(len(cc[0])*len(cc[1]))
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
