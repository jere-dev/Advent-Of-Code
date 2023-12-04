nums = ["0", "1","2", "3", "4", "5", "6", "7", "8", "9"]

lines = open("puzzle-input.txt").read().splitlines()

l = []

numoflines = len(lines)-1
linesize = len(lines[0])-1

for line in range(numoflines+1):
    for c in range(linesize+1):
        if lines[line][c] != "." and lines[line][c] not in nums:
            if line > 0:
                if lines[line-1][c] in nums:
                    l.append((line-1, c))
                if c > 0:
                    if lines[line-1][c-1] in nums:
                        l.append((line-1, c-1))
                if c < linesize:
                    if lines[line-1][c+1] in nums:
                        l.append((line-1, c+1))

            if line < numoflines:
                if lines[line+1][c] in nums:
                    l.append((line+1, c))
                if c > 0:
                    if lines[line+1][c-1] in nums:
                        l.append((line+1, c-1))
                if c < linesize:
                    if lines[line+1][c+1] in nums:
                        l.append((line+1, c+1))

            if c > 0:
                if lines[line][c-1] in nums:
                    l.append((line, c-1))

            if c < linesize:
                if lines[line][c+1] in nums:
                    l.append((line, c+1))

d = {}
for loc in l:
    d[loc[0]] = []

for loc in l:
    d[loc[0]].append(loc[1])

for key in d:
    n = []
    for num in d[key]:
        if num-1 not in n and num+1 not in n and num not in n:
            n.append(num)
    d[key] = n

def postions(size, endpos, num):
    r = []
    for i in range(size):
        r.append({(endpos-i-1):num})
    return r

def GetNumbers(lines):
    numbers = {}

    for line in range(len(lines)):
        num = ""
        i = 0

        for c in range(len(lines[line])):
            if lines[line][c] in nums:
                i += 1
                num = num + lines[line][c]
                if c == len(lines[line])-1:
                    if num != "":
                        if line in numbers:
                            numbers[line] += postions(len(num), c+1, num)
                        else:
                            numbers[line] = postions(len(num), c+1, num)
            elif i > 0:
                    if line in numbers:
                        numbers[line] += postions(len(num), c, num)
                    else:
                        numbers[line] = postions(len(num), c, num)
                    i = 0
                    num = ""
            

    for k in numbers:
        d = {}
        for i in numbers[k]:
            d.update(i)
        numbers[k] = d

    return numbers

numbers = GetNumbers(lines)

# print(d)
# print("-"*45)
# print(numbers)

answer = 0
for k in d:
    for kk in d[k]:
        if kk in numbers[k]:
            answer += int(numbers[k][kk])

print("Part 1: " + str(answer))