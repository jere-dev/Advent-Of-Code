nums = ["1","2", "3", "4", "5", "6", "7", "8", "9"]
lnums = {"one":"one1one", "two":"two2two", "three":"three3three", "four":"four4four", "five":"five5five", "six":"six6six", "seven":"seven7seven", "eight":"eight8eight", "nine":"nine9nine"}

def getNum(line):
    a = []
    for i in line:
        if i in nums:
            a.append(i)
    return int((a[0]+a[-1]))

def wordToNum(line):
    for x in lnums.keys():
        line = line.replace(x, lnums[x])
    return line


answer = 0

for line in open("puzzle-input.txt").read().splitlines():
    answer += getNum(line)

print("Part 1: " + str(answer))


answer = 0

for line in open("puzzle-input.txt").read().splitlines():
    answer += getNum(wordToNum(line))

print("Part 2: " + str(answer))