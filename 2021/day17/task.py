import os

def hits(vx, vy, xmin, xmax, ymin, ymax):  # 6 4
    if vy > 0:
        arch_steps = vy * 2 + 1  # 9
        #vx -= arch_steps
        vy = (vy + 1) * -1  # -5
        if vx - arch_steps >= 0:
            px = sum(range(vx, vx-arch_steps, -1))
            vx -= arch_steps
        else:
            px = sum(range(vx+1))  # 21
            vx = 0
        #vx -= arch_steps
        py = 0
    else:
        px = 0
        py = 0
    while py >= ymin:
        px += vx
        py += vy
        vx = vx - 1 if vx > 0 else 0
        vy -= 1
        if xmin <= px <= xmax and ymin <= py <= ymax:
            return True
    return False

def compute(s: str, part: int):
    ## if single value:
    s = s.strip()
    ## if multiple values in multiple lines
    #lines = s.splitlines()
    #lines = lines[:-1] if lines[-1] == '' else lines
    _, s = s.split(': ')
    sx, sy = s.split(', ')
    _, sxvs = sx.split('=')
    xvs = sxvs.split('..')
    xmin, xmax = int(xvs[0]), int(xvs[1])
    _, syvs = sy.split('=')
    yvs = syvs.split('..')
    ymin, ymax = int(yvs[0]), int(yvs[1])
    res = 0
    max_height = 0
    vy = 156
    while vy > -160:
        for vx in range(170):
            if hits(vx, vy, xmin, xmax, ymin, ymax):
                h = vy*(vy+1)//2
                max_height = h if h > max_height else max_height
                res += 1

        vy -= 1
    return max_height if part == 1 else res

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [112]
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
    print("Part 1:", compute(inp, 1))
    print("Part 2:", compute(inp, 2))

if __name__ == "__main__":
    main()
