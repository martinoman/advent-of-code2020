def oneStar(lines):
    direction = "E"
    directionIndex = 0
    directions = ["E", "S", "W", "N"]
    pos = {"E": 0, "W": 0, "N": 0, "S": 0}
    for line in lines:
        instr = line[0]
        amount = int(line[1:])
        if instr == "E" or instr == "W" or instr == "N" or instr == "S":
            pos[instr] += amount
        elif instr == "F":
            pos[direction] += amount
        else:
            c = int(amount/90)
            if instr == "R":
                directionIndex += c
            else:
                directionIndex -= c
            direction = directions[directionIndex%4]
    print(abs(pos["E"] - pos["W"]) + abs(pos["N"] - pos["S"]))

def twoStar(lines):
    waypointPos = {"E": 10, "W": 0, "N": 1, "S": 0}
    pos = {"E": 0, "W": 0, "N": 0, "S": 0}
    for line in lines:
        instr = line[0]
        amount = int(line[1:])
        if instr == "E" or instr == "W" or instr == "N" or instr == "S":
            waypointPos[instr] += amount
        elif instr == "F":
            pos["E"] += waypointPos["E"]*amount
            pos["W"] += waypointPos["W"]*amount
            pos["N"] += waypointPos["N"]*amount
            pos["S"] += waypointPos["S"]*amount
        else:
            for _ in range(int(amount/90)):
                tempPos = waypointPos.copy()
                if instr == "R":
                    tempPos["E"] = waypointPos["N"]
                    tempPos["S"] = waypointPos["E"]
                    tempPos["W"] = waypointPos["S"]
                    tempPos["N"] = waypointPos["W"]
                else:
                    tempPos["W"] = waypointPos["N"]
                    tempPos["N"] = waypointPos["E"]
                    tempPos["E"] = waypointPos["S"]
                    tempPos["S"] = waypointPos["W"]
                waypointPos = tempPos
    print(abs(pos["E"] - pos["W"]) + abs(pos["N"] - pos["S"]))
            
if __name__ == '__main__':
    file1 = open('data12', 'r')
    lines = file1.read().splitlines()

    oneStar(lines)
    twoStar(lines)
