def oneStar(lines):
    time = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(",") if bus != "x"]
    smallestDiff = 10000000000
    bestbus = -1
    for bus in buses:
        a = time % bus 
        b = bus - a
        if b < smallestDiff:
            smallestDiff = b
            bestbus = bus
    print(bestbus * smallestDiff)

def twoStar(lines):
    buses = [bus for bus in lines[1].split(",")]
    searching = True
    time = 1
    increment = 1
    highestIndex = -1
    while searching:
        time += increment
        busIndex = 0
        for bus in buses:
            if bus == "x":
                busIndex += 1
            else:
                busint = int(bus)
                a = time % busint
                b = busint - a
                if b == busIndex%busint or (a == 0 and busIndex == 0):
                    if busIndex > highestIndex:
                        increment = increment * busint
                        highestIndex = busIndex
                else:
                    break
                if busIndex == len(buses)-1:
                    searching = False
                busIndex += 1
    print(time)
            
if __name__ == '__main__':
    file1 = open('data13', 'r')
    lines = file1.read().splitlines()
    oneStar(lines)
    twoStar(lines)
