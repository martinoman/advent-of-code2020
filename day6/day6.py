def oneStar(answers):
    sum = 0
    answers = ""
    for line in lines:
        line = line.replace("\n", "")
        s = set(line)
        sum += len(s)
    print(sum)

def twoStar(answers):
    sum = 0
    for answer in answers:
        rows = answer.split("\n")
        availableQuestions = rows[0]
        for row in rows:
            if row == "":  # lazy way to handle bad input
                break
            availableQuestions = [letter for letter in availableQuestions if letter in row]
        sum += len(availableQuestions)
    print(sum)

if __name__ == '__main__':
    file1 = open('day6data', 'r')
    lines = file1.read().split("\n\n")

    oneStar(lines)
    twoStar(lines)
    



