rucksack = []
def alp_Pri(alp):
    if ord(alp) <= 90:
        return ord(alp) - 38
    return ord(alp) - 96

for i in open("Day-3-input.txt").read().split("\n"):
    comp1 = []
    comp2 = []
    comp = []
    for item in i:
        comp.append(item)
    
    comp1size = int(len(comp)/2)-1

    for item in range(len(comp)):
        if item <= comp1size:
            comp1.append(comp[item])
        else:
            comp2.append(comp[item])

    rucksack.append([comp1,comp2])

#part 1
priority = []
prisum = 0
for i in rucksack:
   pri = 0
   comp1, comp2 = i
   for item1 in comp1:
       for item2 in comp2:
           if item1 == item2:
               pri = alp_Pri(item1)
   priority.append(pri)
   prisum += pri

print("Part 1:",prisum)

prisum = 0
rucksack = [comp1+comp2 for comp1, comp2 in rucksack]
rucksack = [[rucksack[i],rucksack[i+1],rucksack[i+2]] for i in range(0,len(rucksack), 3) ]

for i in rucksack:
    for char in i[0]:
        if char in i[1]:
            if char in i[2]:
                prisum += alp_Pri(char)
                break;

print("Part 2:",prisum)