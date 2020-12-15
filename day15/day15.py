def bothStar(input, iterations):
    game = {}
    round = 0
    lastWasNew = True
    for i in input:
        game[i] = round
        round += 1
        number = i
    for i in range(len(input)-1, iterations):
        if lastWasNew:
            newNumber = 0
        else:
            newNumber = i - game[number]
        if newNumber in game:
            lastWasNew = False
        else:
            lastWasNew = True
            game[newNumber] = i+1
        game[number] = i
        number = newNumber
    print(number)

if __name__ == '__main__':
    input = [0, 13, 1, 8, 6, 15]
    bothStar(input, 2019)
    bothStar(input, 29999999)
