pairs = []
for i in open("Day-4-input.txt").read().split("\n"):
    pairpair = []
    for j in i.split(","):
        pair = []
        sec1 = int(j.split("-")[0])
        sec2 = int(j.split("-")[1])
        for k in range(sec1, sec2+1):
            pair.append(k)
        pairpair.append(pair)
    pairs.append(pairpair)

contained = 0
for pair in pairs:
    if all(item in pair[0] for item in pair[1]) or all(item in pair[1] for item in pair[0]):
        contained += 1

print("Part 1:",contained)

contained = 0
for pair in pairs:
    for item in pair[0]:
        if item in pair[1]:
            contained += 1
            break;

print("Part 2:",contained)