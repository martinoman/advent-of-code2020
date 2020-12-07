import re

def getColor(bagStr):
    l = bagStr.split("")
    if not re.match("\d", l[0]):
        return l[0] + " " + l[1]
    
    return bagStr.replace("")

def canCarryGold(color, rules):
    if color == "no other":
        return False
    if "shiny gold" in rules[color]:
        return True
    else:
        for rule in rules[color]:
            if canCarryGold(rule, rules):
                return True

def oneStar(lines):
    rules = {}
    for line in lines:
        line = re.split("contain", line)
        contain = [re.sub("(\d |, | bags?|\.)", "", s).strip() for s in line[1].split(", ")]
        rules[line[0].replace(" bags ", "")] = contain
    a = [b for b in rules if canCarryGold(b, rules)]
    print(len(a))


if __name__ == '__main__':
    file1 = open('day7data', 'r')
    lines = file1.read().splitlines()

    oneStar(lines)
