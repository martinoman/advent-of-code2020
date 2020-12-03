import math
import numpy

file1 = open('day3data', 'r')
lines = file1.readlines()

slope = [line for line in lines]
repeatLength = len(slope[0].strip())

def step(x,y, position):
    position[0] += x
    position[1] += y

def getLocation(x,y):
    if y >= len(slope):
        return 1
    slopeStrip = slope[y].strip()
    if x >= repeatLength:
        multiplier = math.ceil((x+1)/repeatLength)
        slopeStrip = slopeStrip*multiplier
    return slopeStrip[x]

def countHits(steps):
    position=[0,0]
    xStep = steps[0]
    yStep = steps[1]
    treehits = 0
    for i in range(0, len(slope)-1):
        step(xStep, yStep, position)
        location = getLocation(position[0], position[1])
        if location == '#':
            treehits += 1
    return treehits

def main():
    result = 1
    steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    result = map(countHits, steps)
    answer = numpy.prod(list(result))
    print(answer)

main()

