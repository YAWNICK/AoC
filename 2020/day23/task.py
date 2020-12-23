import os


class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None


class CLL:

    def __init__(self):
        self.head = None
        self.tail = None  # tail is only needed for filling the cll
        self.nr = {}  # maps numbers to their Node

    def isEmpty(self):
        return self.head == None

    def append(self, val):
        new = Node(val)
        if self.isEmpty():
            new.next = new
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.next = self.head
            self.tail = new
        self.nr[val] = new
    
    def cut(self, prev):  # cut the node after prev
        node = prev.next
        prev.next = node.next
        return node
    
    def insertAfter(self, node, newnode):
        newnode.next = node.next
        node.next = newnode
    
    def show(self):
        s = str(self.head.val)
        i = self.head
        while i.next != self.head:
            i = i.next
            s += ',' + str(i.val)
        print(s)
    
    def find_solution(self):
        i = self.head
        while i.val != 1:
            i = i.next
        n1 = i.next.val
        n2 = i.next.next.val
        print(n1, n2)
        return n1 * n2

# Part 2:
# The more efficient solution wtill with some magic numbers...
def compute2(s):
    nums = list(map(int, list(s)))
    cll = CLL()
    for n in nums:
        cll.append(n)
    for n in range(10, 1000001):
        cll.append(n)
    curr = cll.head
    for i in range(10000000):
        out = [cll.cut(curr), cll.cut(curr), cll.cut(curr)]
        outvals = list(map(lambda x: x.val, out))
        dstval = curr.val
        while True:
            dstval -= 1
            if dstval < 1:
                dstval = 1000000
            if dstval not in outvals:
                break
        node = cll.nr[dstval]
        cll.insertAfter(node, out.pop())
        cll.insertAfter(node, out.pop())
        cll.insertAfter(node, out.pop())
        curr = curr.next
    return cll.find_solution()


# Part 1: 
# The naive solution full of magic numbers
def compute(s: str):
    nums = list(map(int, list(s)))
    curr = nums[0]
    cind = 0
    clen = len(nums)
    for i in range(100):
        popind = (cind+1) % 9
        out = [nums.pop(popind)]
        popind = (popind) % 8
        out.append(nums.pop(popind))
        popind = popind % 7
        out.append(nums.pop(popind))
        dst = curr
        while True:
            dst -= 1
            if dst < 1:
                dst = 9
            if dst not in out:
                break
        ind = nums.index(dst)
        nums = nums[:ind + 1] + out + nums[ind + 1:]
        cind = (nums.index(curr) + 1) % 9
        curr = nums[cind]
    # convert to actual solution manually
    return nums

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
    inp = '193467258'
    print("Part 1:", compute(inp))
    print("Part 2:", compute2(inp))

if __name__ == "__main__":
    main()
