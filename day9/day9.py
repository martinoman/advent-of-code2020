def oneStar(lines):
    preambleLength = 25
    currentIndex = preambleLength
    possibleNumbers = []
    for number in lines[preambleLength:]:
        possibleNumbers = getPossibleNumbers(currentIndex, preambleLength, lines)
        currentIndex += 1
        if int(number) not in possibleNumbers:
            print(number)
            break
    
def getPossibleNumbers(index, length, lines):
    possibleNumbers = []
    for n1 in lines[index-length:index]:
        for n2 in lines[index-length:index]:
            if n1 != n2:
                possibleNumbers.append(int(n1)+int(n2))
    return possibleNumbers

def twoStar(lines):
    answer = 57195069
    startIndex = 0
    endIndex = 1
    answerRange = []
    currentSum = 0
    searching = True
    while searching:
        currentSum = sum([int(n) for n in lines[startIndex:endIndex]])
        if currentSum == answer:
            answerRange = [int(n) for n in lines[startIndex:endIndex]]
            searching = False
        elif currentSum > answer:
            currentSum = 0
            startIndex += 1
            endIndex = startIndex + 1
        else:
            endIndex += 1
    print(max(answerRange) + min(answerRange))

if __name__ == '__main__':
    file1 = open('day9data', 'r')
    lines = file1.read().splitlines()
    oneStar(lines)
    twoStar(lines)
