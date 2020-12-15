import os

# Part 1:
# (way inefficient)

def compute(s):
    hm = {}
    for n in s:
        hm.setdefault(n, [False, 0, 0])
        for m in hm:
            hm[m][1] += 1
    nums = []
    nums += s
    numl = len(nums)
    while numl < 2020:
        last = nums[-1]
        if hm[last][0] is False:
            new = 0
        else:
            new = hm[last][2]
        if new in nums:
            l = hm[new]
            l[0] = True
            l[2] = l[1]
            l[1] = 0
        else:
            hm[new] = [False, 0, 0]
        nums.append(new)
        numl += 1
        for m in hm:
            hm[m][1] += 1
    return nums[-1]

# Part 2:
# a more efficient solution

def compute2(s):
    ind = {}
    for n in s:
        ind[n] = s.index(n) + 1
    last = s[-1]
    numl = len(s)  # this is the counter 
    while numl < 30000000:
        l = ind.setdefault(last, 0)
        if l == 0:
            new = 0
        else:
            new = numl - l
        ind[last] = numl 
        last = new
        numl += 1
    return last

# setup

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
    #inp = read_input("input.txt")
    inp = [0, 12, 6, 13, 20, 1, 17]
    print("Part 1:", compute(inp))
    print("Part 2:", compute2(inp))

if __name__ == "__main__":
    main()
