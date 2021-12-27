import os
from functools import reduce
from operator import mul

vs = 0

class Packet:

    def __init__(self, version, tpe, val=None, subp=[]):
        self.version = version
        self.type = tpe
        self.val = val
        self.subp = subp

    def __str__(self):
        s = f'v:{self.version},t:{self.type}'
        if self.type == 4:
            s += f', val:{self.val}'
        else:
            s += ', subp:('
            for p in self.subp:
                s += str(p) + ';'
            s += ')'
        return s

    def eval(self):
        tpe = self.type
        if tpe == 0:
            return sum(map(lambda p: p.eval(), self.subp))
        elif tpe == 1:
            return reduce(mul, map(lambda p: p.eval(), self.subp), 1)
        elif tpe == 2:
            return min(map(lambda p: p.eval(), self.subp))
        elif tpe == 3:
            return max(map(lambda p: p.eval(), self.subp))
        elif tpe == 4:
            return self.val
        elif tpe == 5:
            return int(self.subp[0].eval() > self.subp[1].eval())
        elif tpe == 6:
            return int(self.subp[0].eval() < self.subp[1].eval())
        elif tpe == 7:
            return int(self.subp[0].eval() == self.subp[1].eval())

def parsePacket(text):
    global vs
    version, tpe, text = int(text[:3], 2), int(text[3:6], 2), text[6:]
    vs += version
    bits_read = 6
    if tpe == 4:
        vstr = ''
        part, text = text[:5], text[5:]
        while part[0] != '0':
            vstr += part[1:]
            bits_read += 5
            part, text = text[:5], text[5:]
        vstr += part[1:]
        bits_read += 5
        return Packet(version, tpe, val=int(vstr, 2)), bits_read, text
    else:
        mode, text = text[:1], text[1:]
        bits_read += 1
        if mode == '0':
            length, text = int(text[:15], 2), text[15:]
            bits_read += 15
            subps = []
            while length > 0:
                subp, read, text = parsePacket(text)
                subps.append(subp)
                bits_read += read
                length -= read
            return Packet(version, tpe, subp=subps), bits_read, text
        else:
            length, text = int(text[:11], 2), text[11:]
            bits_read += 11
            subps = []
            while length > 0:
                subp, read, text = parsePacket(text)
                subps.append(subp)
                bits_read += read
                length -= 1
            return Packet(version, tpe, subp=subps), bits_read, text



def compute(s: str, part: int):
    global vs
    vs = 0
    s = s.strip()
    b = str(bin(int(s, 16)))[2:]
    first = int(s[0], 16)
    if first < 8:
        b = '0' + b
    if first < 4:
        b = '0' + b
    if first < 2:
        b = '0' + b
    if first < 1:
        b = '0' + b
    p, read, text = parsePacket(b)
    #print(vs)
    #print(p.eval())
    return vs if part == 1 else p.eval()

def read_input(filepath: str) -> str:
    inp = ""
    with open(filepath, 'r') as f:
        inp = f.read()
    return inp

def run_tests():
    print("-----TESTS-----")
    # Fill solutions with should values
    solutions = [16, 12]
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
