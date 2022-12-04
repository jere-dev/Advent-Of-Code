import time

def getadj(x,y,maxX,maxY):
    adj = []
    if x > 0:               #checks if x is not 0
        adj.append((x-1,y))
        if y > 0:
            adj.append((x-1,y-1))

    if x < maxX:            #checks if x is not end of list
        adj.append((x+1,y)) 
        if y < maxY:
            adj.append((x+1,y+1))

    if y > 0:               #checks if y is not 0
        adj.append((x,y-1))
        if x < maxX:
            adj.append((x+1,y-1))

    if y < maxY:            #checks if y is not end of list 
        adj.append((x,y+1))
        if x > 0:
            adj.append((x-1,y+1))
    
    return adj

def flash_wave(x, y, maxX, maxY, grid):
    flashed = []
    for x, y in getadj(x, y, maxX, maxY):
        if grid[x][y] != 10:
            grid[x][y] += 1
            if grid[x][y] == 10:
                flashed.append((x, y))
    return flashed

def printoct(input):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for row in input:
        print(row)

dumboOctopuses = [list(map(int,list(line))) for line in open("../../Day-11-input.txt").read().split("\n")] 
step = 0
maxY = len(dumboOctopuses)-1
maxX = len(dumboOctopuses[0])-1
flashes = 0
Part1 = 0

print("before steps")
printoct(dumboOctopuses)
print()
syncStep = 0

while True:
    flashed = []
    for row in range(len(dumboOctopuses)):
        for octopus in range(len(dumboOctopuses[row])):
            dumboOctopuses[row][octopus] += 1
            if dumboOctopuses[row][octopus] == 10:
                flashed.append((row, octopus))

    for row, octopus in flashed:
        flashed += flash_wave(row, octopus, maxX, maxY, dumboOctopuses)

    flashes += len(flashed)

    for row, octopus in flashed:
        dumboOctopuses[row][octopus] = 0

    printoct(dumboOctopuses)
    print()
    print("step ",step+1)
    time.sleep(1)

    if step+1 == 100:
        Part1 = flashes

    if len(flashed) == 100:
        syncStep = step + 1
        break

    step += 1



print("\n\n\nFalshes: ", Part1)
print("all octopuses flash at step: " , syncStep) 
#kinda visualization cuoldnt change color of 0 