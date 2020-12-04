import re

file1 = open('day4data', 'r')
lines = file1.readlines()

def isfieldValid(field):
    try:
        if field[0] == "byr":
            return int(field[1]) >= 1920 and int(field[1]) <=2002
        elif field[0] == "iyr":
            return int(field[1]) >= 2010 and int(field[1]) <= 2020
        elif field[0] == "eyr":
            return int(field[1]) >= 2020 and int(field[1]) <= 2030
        elif field[0] == "hgt":
            length = int(field[1][:-2])
            if field[1][-2:] == "cm":
                return length >= 150 and length <= 193
            else:
                return length >= 59 and length <= 76
        elif field[0] == "hcl":
            match = re.fullmatch("#[a-f0-9]{6}", field[1])
            if match:
                return True
            return False
        elif field[0] == "ecl":
            return field[1] in ["amb", "blu", "brn",  "gry",  "grn",  "hzl",  "oth"]
        elif field[0] == "pid":
            match = re.fullmatch("[0-9]{9}", field[1])
            if match:
                return True
            return False
    except:
        return False
    

def checkFields(passport):
    reqFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = True
    for field in passport:
        fieldPair = field.split(":")
        if fieldPair[0] in reqFields:
            reqFields.remove(fieldPair[0])
        if not isfieldValid(fieldPair) and fieldPair[0] != "cid":
            valid = False
    return valid and len(reqFields) == 0

def main():
    passport = []
    passports = []
    for line in lines:
        if line.strip() == "":
            passports.append(passport)
            passport = []
        else:
            passport += re.split("\s", line.strip())

    passports.append(passport) #Handles the punk ass last passport that doesnt wanna work 😡

    validPassports = [passport for passport in passports if checkFields(passport)]
    print(len(validPassports))

main()