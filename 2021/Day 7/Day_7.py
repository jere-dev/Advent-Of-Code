from math import inf

#open and store int in pos
Pos = []
for n in open('Day-7-input.txt').read().split(','):
    Pos.append(int(n))
#get get part1 and part2 
Part1 = []
Part2 = []
for p in range(max(Pos)):
    fuel = 0
    fuel2 = 0
    for p1 in Pos:
        fuel += abs(p1 - p)
        #Triangle number formula T = (n)(n + 1) / 2
        fuel2 += int((abs(p1 - p)+1)*(abs(p1 - p)/2))
    Part1.append(fuel)
    Part2.append(fuel2)

#print the lowest value in part1 and part2
print("Part1: ",min(Part1))
print("Part2: ",min(Part2))