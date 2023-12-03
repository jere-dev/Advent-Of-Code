restrictions = {'blue': 14, 'red': 12, 'green': 13}

def possible(line):
    line = line.replace(";", ",")
    line = line.replace(":", ",")
    line = [l.split() for l in line.split(",")]
    line[0] = [line[0][1], line[0][0]]
    
    for i in line:
        if i[1] == "Game":
            continue
        if restrictions[i[1]] < int(i[0]):
            return 0
    return int(line[0][0])

def power(line):
    line = line.replace(";", ",")
    line = line.replace(":", ",")
    line = [l.split() for l in line.split(",")]
    line[0] = [line[0][1], line[0][0]]
    
    val = {'blue': 0, 'red': 0, 'green': 0}

    for i in line:
        if i[1] == "Game":
            continue
        if val[i[1]] < int(i[0]):
            val[i[1]] = int(i[0])
    return val["blue"]*val["red"]*val["green"]

answer = 0
for line in open("puzzle-input.txt").read().splitlines():
    answer += possible(line)

print("Part 1: " + str(answer))

answer = 0
for line in open("puzzle-input.txt").read().splitlines():
    answer += power(line)

print("Part 2: " + str(answer))