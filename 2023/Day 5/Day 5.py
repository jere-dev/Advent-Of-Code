lines = open("puzzle-input.txt").read().splitlines()

diction = {}
curmap = ""

def mapNumEff(l, num):
    low = l[1]
    high = l[1]+l[2]-1
    if num >= low and num <= high:
        num = l[0] + (num-low)
        return num
    return - 1

def mappedNum(num, d):
    nextnum = num
    for k in d:
        if k == "seeds":
            continue
        for ll in d[k]:
            idk = mapNumEff(ll, nextnum)
            if idk != -1:
                nextnum = idk
                break
    return nextnum

for line in lines:
    if "seeds: " in line:
        curmap = "seeds"
        line = line.split(": ")
        diction[line[0]] = [int(num) for num in line[1].split()] 
    elif line == "seed-to-soil map:":
        curmap = "seed-to-soil"
        line = curmap
    elif line == "soil-to-fertilizer map:":
        curmap = "soil-to-fertilizer"
        line = curmap
    elif line == "fertilizer-to-water map:":
        curmap = "fertilizer-to-water"
        line = curmap
    elif line == "water-to-light map:":
        curmap = "water-to-light"
        line = curmap
    elif line == "light-to-temperature map:":
        curmap = "light-to-temperature"
        line = curmap
    elif line == "temperature-to-humidity map:":
        curmap = "temperature-to-humidity"
        line = curmap
    elif line == "humidity-to-location map:":
        curmap = "humidity-to-location"
        line = curmap

    if line != curmap and curmap != "seeds":
        if curmap in diction:
            diction[curmap] = diction.get(curmap, []) + ([int(num) for num in line.split()])
        else:
            diction[curmap] = [int(num) for num in line.split()] 

for k in diction:
    if k == "seeds":
        continue
    diction[k] = [diction[k][i * 3:(i + 1) * 3] for i in range((len(diction[k]) + 3 - 1) // 3 )]

minn = None
for num in diction["seeds"]:
    nnnnn = mappedNum(num, diction)
    if minn == None:
        minn = nnnnn
    elif minn > nnnnn:
        minn = nnnnn

print("Part 1: ", minn)

minn = None
for i in range(0, len(diction["seeds"]), 2):
    for j in range(diction["seeds"][i], diction["seeds"][i]+diction["seeds"][i+1]):
        nnnnn = mappedNum(j, diction)
        if minn == None:
            minn = nnnnn
        elif minn > nnnnn:
            minn = nnnnn

print("Part 2: ", minn)