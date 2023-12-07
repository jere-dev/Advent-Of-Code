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

l = []
for num in diction["seeds"]:
    nextnum = num
    for k in diction:
        if k == "seeds":
            continue
        for ll in diction[k]:
            idk = mapNumEff(ll, nextnum)
            if idk != -1:
                nextnum = idk
                break
    l.append(nextnum)

print("Part 1: ", min(l))

seeds = []
for i in range(len(diction["seeds"])//2):
    for i in range(diction["seeds"][i], diction["seeds"][i]+diction["seeds"][i+1]):
        seeds.append(i)
diction["seeds"] = seeds

print(diction["seeds"])

l = []
for num in diction["seeds"]:
    nextnum = num
    for k in diction:
        if k == "seeds":
            continue
        for ll in diction[k]:
            idk = mapNumEff(ll, nextnum)
            if idk != -1:
                nextnum = idk
                break
    l.append(nextnum)

print("Part 2: ", min(l))