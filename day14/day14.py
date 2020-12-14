import re, math

def oneStar(lines):
    mask = ""
    mem = {}
    for line in lines:
        a = line.split("=")
        if a[0].strip() == "mask":
            mask = a[1].strip()
        else:
            memLoc = a[0][4:-2]
            number = a[1].strip()
            mem[memLoc] = applyMask(number, mask)
    print(sum(mem.values()))

def applyMask(number, mask):
    modMask = mask.replace("X", "1")
    stepOne = int(number) & int(modMask,2)
    modMask = mask.replace("X", "0")
    stepTwo = stepOne | int(modMask,2)
    return stepTwo

def twoStar(lines):
    mem = {}
    allMemLocs = []
    for line in lines:
        a = line.split("=")
        if a[0].strip() == "mask":
            mask = a[1].strip()
        else:
            memLoc = a[0][4:-2]
            number = int(a[1].strip())
            allMemLocs = getAllMemLocs(memLoc, mask)
            for loc in allMemLocs:
                mem[int(loc,2)] = number
    print(sum(mem.values()))
                
def getAllMemLocs(addr, mask):
    floatingIdx = [m.start() for m in re.finditer("X", mask)]
    floatingIdx.reverse()
    allAddrs = []
    longAddr = f'{int(addr):036b}'
    potAddr = ""
    for i, letter in enumerate(mask):
        if letter == "1":
            potAddr += letter
        elif letter == "0":
            potAddr += longAddr[i]
        else:
            potAddr += "X"
    for i in range(2**len(floatingIdx)):
        tempAddr = potAddr
        binaryStr = f'{i:036b}'
        for j, floatIdx in enumerate(floatingIdx):
            tempAddr = tempAddr[:floatIdx] + binaryStr[-(j+1)] + tempAddr[floatIdx+1:]
        allAddrs.append(tempAddr)
    return allAddrs

if __name__ == '__main__':
    file1 = open('data14', 'r')
    lines = file1.read().splitlines()
    oneStar(lines)
    twoStar(lines)
