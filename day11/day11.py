def oneStar(lines):
    changed = True
    occSeats = 0
    updatedSeating, changed = updateSeatingOneStar(lines)
    while changed:
        updatedSeating, changed = updateSeatingOneStar(updatedSeating)
    for line in updatedSeating:
        occSeats += line.count("#")
    print(occSeats)

def updateSeatingOneStar(matrix):
    columns = len(matrix[0]) - 1
    rows = len(matrix) - 1
    newGraph = ["" for _ in range(rows+1)]
    changed = False
    for y, line in enumerate(matrix):
        updatedRow = ""
        for x, pos in enumerate(line):
            s = ""
            occNeigh = 0
            if x == 0 and y == 0:  # Top left corner
                s += matrix[y][x+1]
                s += matrix[y+1][x+1]
                s += matrix[y+1][x]
            elif x == columns and y == 0:  # Top right corner
                s += matrix[y][x-1]
                s += matrix[y+1][x-1]
                s += matrix[y+1][x]
            elif x == 0 and y == rows:  # Bottom left
                s += matrix[y-1][x]
                s += matrix[y-1][x+1]
                s += matrix[y][x+1]
            elif x == columns and y == rows:  # Bottom right
                s += matrix[y-1][x]
                s += matrix[y-1][x-1]
                s += matrix[y][x-1]
            elif x == 0:  # Left side
                s += matrix[y-1][x]
                s += matrix[y-1][x+1]
                s += matrix[y][x+1]
                s += matrix[y+1][x+1]
                s += matrix[y+1][x]
            elif y == 0:  # Top row
                s += matrix[y][x-1]
                s += matrix[y+1][x-1]
                s += matrix[y+1][x]
                s += matrix[y+1][x+1]
                s += matrix[y][x+1]
            elif x == columns:  # Right side
                s += matrix[y-1][x]
                s += matrix[y-1][x-1]
                s += matrix[y][x-1]
                s += matrix[y+1][x-1]
                s += matrix[y+1][x]
            elif y == rows:  # Bottom row
                s += matrix[y][x-1]
                s += matrix[y-1][x-1]
                s += matrix[y-1][x]
                s += matrix[y-1][x+1]
                s += matrix[y][x+1]
            else:  # Everything else
                s += matrix[y-1][x-1]
                s += matrix[y-1][x]
                s += matrix[y-1][x+1]
                s += matrix[y][x+1]
                s += matrix[y+1][x+1]
                s += matrix[y+1][x]
                s += matrix[y+1][x-1]
                s += matrix[y][x-1]
            if matrix[y][x] == "L" and s.count("#") == 0:
                updatedRow += "#"
                changed = True
            elif matrix[y][x] == "#" and s.count("#") >= 4:
                updatedRow += "L"
                changed = True
            else:
                updatedRow += matrix[y][x]
        newGraph[y] = updatedRow
    return newGraph, changed


def twoStar(lines):
    changed = True
    occSeats = 0
    updatedSeating, changed = updateSeatingTwoStar(lines)
    while changed:
        updatedSeating, changed = updateSeatingTwoStar(updatedSeating)
    for line in updatedSeating:
        occSeats += line.count("#")
    print(occSeats)


def updateSeatingTwoStar(matrix):
    columns = len(matrix[0]) - 1
    rows = len(matrix) - 1
    newGraph = ["" for _ in range(rows+1)]
    changed = False
    for y, line in enumerate(matrix):
        updatedRow = ""
        for x, pos in enumerate(line):
            s = ""
            if x == 0 and y == 0:  # Top left corner
                s += findInDirection("e", x, y, matrix)
                s += findInDirection("se", x, y, matrix)
                s += findInDirection("s", x, y, matrix)
            elif x == columns and y == 0:  # Top right corner
                s += findInDirection("w", x, y, matrix)
                s += findInDirection("sw", x, y, matrix)
                s += findInDirection("s", x, y, matrix)
            elif x == 0 and y == rows:  # Bottom left
                s += findInDirection("n", x, y, matrix)
                s += findInDirection("ne", x, y, matrix)
                s += findInDirection("e", x, y, matrix)
            elif x == columns and y == rows:  # Bottom right
                s += findInDirection("n", x, y, matrix)
                s += findInDirection("nw", x, y, matrix)
                s += findInDirection("w", x, y, matrix)
            elif x == 0:  # Left side
                s += findInDirection("n", x, y, matrix)
                s += findInDirection("ne", x, y, matrix)
                s += findInDirection("e", x, y, matrix)
                s += findInDirection("se", x, y, matrix)
                s += findInDirection("s", x, y, matrix)
            elif y == 0:  # Top row
                s += findInDirection("w", x, y, matrix)
                s += findInDirection("sw", x, y, matrix)
                s += findInDirection("s", x, y, matrix)
                s += findInDirection("se", x, y, matrix)
                s += findInDirection("e", x, y, matrix)
            elif x == columns:  # Right side
                s += findInDirection("n", x, y, matrix)
                s += findInDirection("nw", x, y, matrix)
                s += findInDirection("w", x, y, matrix)
                s += findInDirection("sw", x, y, matrix)
                s += findInDirection("s", x, y, matrix)
            elif y == rows:  # Bottom row
                s += findInDirection("w", x, y, matrix)
                s += findInDirection("nw", x, y, matrix)
                s += findInDirection("n", x, y, matrix)
                s += findInDirection("ne", x, y, matrix)
                s += findInDirection("e", x, y, matrix)
            else:  # Everything else
                s += findInDirection("se", x, y, matrix)
                s += findInDirection("n", x, y, matrix)
                s += findInDirection("ne", x, y, matrix)
                s += findInDirection("e", x, y, matrix)
                s += findInDirection("s", x, y, matrix)
                s += findInDirection("sw", x, y, matrix)
                s += findInDirection("w", x, y, matrix)
                s += findInDirection("nw", x, y, matrix)
            if matrix[y][x] == "L" and s.count("#") == 0:
                updatedRow += "#"
                changed = True
            elif matrix[y][x] == "#" and s.count("#") >= 5:
                updatedRow += "L"
                changed = True
            else:
                updatedRow += matrix[y][x]
        newGraph[y] = updatedRow
    return newGraph, changed

def findInDirection(dir, x, y, matrix):
    xn = x
    yn = y
    char = ""
    cont = True
    while cont:
        if dir == "s":
            yn += 1
        elif dir == "sw":
            # print("a")
            xn += -1
            yn += 1
        elif dir == "w":
            # print("b")
            xn += -1
        elif dir == "nw":
            # print("c")
            xn += -1
            yn += -1
        elif dir == "n":
            # print("d")
            yn += -1
        elif dir == "ne":
            # print("e")
            yn += -1
            xn += 1
        elif dir == "e":
            # print("f")
            xn += 1
        elif dir == "se":
            # print("g")
            xn += 1
            yn += 1
        if xn >= len(matrix[0]) or xn < 0 or yn >= len(matrix) or yn < 0:
            break
            cont = False
        char = matrix[yn][xn]
        if char == "#" or char == "L":
            break
    return char


if __name__ == '__main__':
    file1 = open('day11data', 'r')
    lines = file1.read().splitlines()

    # oneStar(lines)
    twoStar(lines)
