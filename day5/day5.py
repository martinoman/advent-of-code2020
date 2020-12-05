def oneStar(indexes):
    print(max(indexes))

def twoStar(indexes):
    indexes.sort()
    currentIndex = indexes[0]
    for index in indexes:
        if index != currentIndex:
            break
        else:
            currentIndex += 1
    print(index)

def findIndex(boardingPass):
    low = 0
    high = 127
    dist = 127
    for i, letter in enumerate(boardingPass):
        if i == 7:
            row = high
            low = 0
            high = 7
            dist = 7
        dist = round(dist/2)
        if letter == "B" or letter == "R":
            low += dist
        else:
            high -= dist
    column = low
    return row * 8 + column

if __name__ == '__main__':
    file1 = open('day5data', 'r')
    lines = file1.read().splitlines()
    indexes = [findIndex(boardingPass) for boardingPass in lines]

    oneStar(indexes)
    twoStar(indexes)
    
    
