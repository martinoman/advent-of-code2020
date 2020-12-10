from itertools import chain, combinations
from functools import reduce

def oneStar(lines):  
    currentJolt = 0
    oneJoltDiff = 0
    threeJoltDiff = 0
    for line in lines:
        if currentJolt + 1 == line:
            oneJoltDiff += 1
        elif currentJolt + 3 == line:
            threeJoltDiff += 1
        currentJolt = line 
    threeJoltDiff += 1 #For the jump into the machine
    print(oneJoltDiff * threeJoltDiff)

if __name__ == '__main__':
    file1 = open('day10data', 'r')
    lines = file1.read().splitlines()
    sortedLines = [int(a) for a in lines]
    sortedLines.sort()
    oneStar(sortedLines)
