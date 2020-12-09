import os

def somesum(n, l):
    for i in l:
        for j in l:
            if i != j and i + j == n:
                return True
    return False

def compute(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    lines = list(map(int, lines))
    for i in range(25, len(lines)):
        n = lines[i]
        nums = lines[i-25:i]
        if not somesum(n, nums):
            return n
    return None

def compute2(s: str):
    ## if single value:
    #s = s.strip()
    ## if multiple values in multiple lines
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    lines = list(map(int, lines))
    n = 88311122
    for i in range(len(lines)):
        nums = [lines[i]]
        j = 1
        while sum(nums) < n:
            nums.append(lines[i+j])
            j += 1
        if sum(nums) == n:
            return min(nums) + max(nums)

# alternative solution for part 2
def compute2_alt(s: str):
    lines = s.splitlines()
    lines = lines[:-1] if lines[-1] == '' else lines
    lines = list(map(int, lines))
    n = 88311122
    nums = [lines[0]]
    lo, hi = 0, 0
    while (s := sum(nums)) != n:
        if s < n:
            nums.append(lines[hi + 1])
            hi += 1
        else:
            nums = nums[1:]
            lo += 1
    return min(nums) + max(nums)

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
    print("Part 1:", compute(inp))
    print("Part 2:", compute2(inp))
    print("Part 2 alt:", compute2_alt(inp))

if __name__ == "__main__":
    main()
