def oneStar(lines):
    acc = 0
    currentLine = 0
    instructionsRan = []
    while currentLine not in instructionsRan:
        instruction = lines[currentLine]
        instructionsRan.append(currentLine)
        if instruction[:3] == "acc":
            acc += int(instruction[4:])
            currentLine += 1
        elif instruction[:3] == "nop":
            currentLine += 1
        else:
            currentLine += int(instruction[4:])
    print(acc)

def twoStar(lines):
    acc = 0
    currentLine = 0
    instructionsRan = []
    possibleNopOrJmp = []
    findingError = True
    while findingError:
        instruction = lines[currentLine]
        if currentLine in instructionsRan:
            for index in possibleNopOrJmp:
                if doesProgramTerminate(lines.copy(), index):
                    changeIndex = index
                    findingError = False
                    break
        instructionsRan.append(currentLine)
        if instruction[:3] == "acc":
            currentLine += 1
        elif instruction[:3] == "nop":
            possibleNopOrJmp.append(currentLine)
            currentLine += 1
        else:
            possibleNopOrJmp.append(currentLine)
            currentLine += int(instruction[4:])
    findingAnswer = True
    currentLine = 0
    if lines[changeIndex][:3] == "nop":
        lines[changeIndex] = lines[changeIndex].replace("nop", "jmp")
    else:
        lines[changeIndex] = lines[changeIndex].replace("jmp", "nop")
    while findingAnswer:
        try:
            instruction = lines[currentLine]
        except:
            findingAnswer = False
            break
        if instruction[:3] == "acc":
            acc += int(instruction[4:])
            currentLine += 1
        elif instruction[:3] == "nop":
            currentLine += 1
        else:
            currentLine += int(instruction[4:])
    print(acc)
    
def doesProgramTerminate(alteredLines, changeIndex):
    run = True
    currentLine = 0
    instructionsRan = []
    if alteredLines[changeIndex][:3] == "nop":
        alteredLines[changeIndex] = alteredLines[changeIndex].replace("nop", "jmp")
    else:
        alteredLines[changeIndex] = alteredLines[changeIndex].replace("jmp", "nop")
    while run:
        try:
            instruction = alteredLines[currentLine]
        except:
            return True
        if currentLine in instructionsRan:
            return False
        instructionsRan.append(currentLine)
        if instruction[:3] == "acc":
            currentLine += 1
        elif instruction[:3] == "nop":
            currentLine += 1
        else:
            currentLine += int(instruction[4:])

#Crazy code! Can be refactored into something much more beautiful, but not right now hehe
if __name__ == '__main__':
    file1 = open('day8data', 'r')
    lines = file1.read().splitlines()

    oneStar(lines)
    twoStar(lines)
