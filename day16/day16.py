import re

def oneStar(lines):
    span = [False for _ in range(1000)]
    a = 0
    sum = 0
    for line in lines:
        if line == "":
            a += 1
            continue
        if a == 0:
            b = re.split(r':', line)
            nums = re.split(r'[^\d]+', b[1].strip())
            for i in range(int(nums[0]), int(nums[1])+1):
                span[i] = True
            for i in range(int(nums[2]), int(nums[3])+1):
                span[i] = True
        elif a == 1:
            print("My ticket")
        elif a == 2:
            if line == "nearby tickets:":
                continue
            nums = line.split(",")
            for num in nums:
                if not span[int(num)]:
                    sum += int(num)
    print(sum)
    
if __name__ == '__main__':
    file1 = open('data16', 'r')
    lines = file1.read().splitlines()
    oneStar(lines)
