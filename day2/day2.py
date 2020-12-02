import re
file1 = open('day2data', 'r')
Lines = file1.readlines()
counter = 0
low_limit = 0
high_limit = 0
char = ""
password = ""
for line in Lines:
    splitted = re.split("[-\s]", line.strip())
    low_limit = int(splitted[0]) - 1
    high_limit = int(splitted[1]) - 1
    char = splitted[2][0]
    password = splitted[3]
    # char_count = password.count(char)
    # if char_count >= low_limit and char_count <= high_limit:  
    #     counter += 1
    if (password[low_limit] == char) != (password[high_limit] == char):
        counter += 1
print(counter)


