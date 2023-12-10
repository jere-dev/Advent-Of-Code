lines = [[int(num) for num in line.split()[1::]] for line in open("puzzle-input.txt").read().splitlines()]

def wins(time, rec):
    wins = 0
    for i in range(1, time):
        d = (time-i)*i
        if d > rec:
            wins += 1
    return wins

answer = 1
for num in range(len(lines[0])):
    answer *= wins(lines[0][num], lines[1][num])

print("Part 1:", answer)

ninput = []
for line in lines:
    linenum = ""
    for num in line:
        linenum += str(num)
    ninput.append(int(linenum))
lines = ninput

answer = wins(lines[0], lines[1])

print("Part 2:", answer)