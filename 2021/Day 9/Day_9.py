def getadj(x,y,maxX,maxY):
    adj = []
    if x > 0:               #checks if x is not 0
        adj.append((x-1,y))
    if x < maxX:            #checks if x is not end of list
        adj.append((x+1,y))
    if y > 0:               #checks if y is not 0
        adj.append((x,y-1))
    if y < maxY:            #checks if y is not end of list 
        adj.append((x,y+1))
    
    return adj

def Islowpoint(x,y,maxX,maxY,input):
    adjPoints = getadj(x,y,maxX,maxY)       #get adj points 
    minVal = [] 
    for adjPoint in adjPoints:              #get min value in adjPoints
        adj_x,adj_y = adjPoint
        minVal.append(input[adj_x][adj_y])
    minVal = min(minVal)

    if input[x][y] < minVal:                #check if lowPoint 
        return True
    return False

def getbasin(x,y,maxX,maxY,input):
    basin = []   
    adjPoints = getadj(x,y,maxX,maxY)

    for adjPoint in adjPoints:
        x,y = adjPoint
        if input[x][y] != 9: 
            basin.append(adjPoint)                  #check if adjpoint is not nine add to basin 
            for point in getadj(x,y,maxX,maxY):     
                if adjPoints.count(point) == 0:
                    adjPoints.append(point)         #check if point is not in adjPoints add to adjPoints

    return basin           


#open file and store heightmap
heightmap = []
for line in open("Day-9-input.txt").read().splitlines():
    l = []
    for num in list(line):
        l.append(int(num))
    heightmap.append(l)

#get heightmap ends
maxX = len(heightmap)-1
maxY = len(heightmap[0])-1


lowPoint = []
Part1 = []
for x in range(len(heightmap)):
    for y in range(len(heightmap[x])):
        if Islowpoint(x,y,maxX,maxY,heightmap): #check if lowpoint
            lowPoint.append((x,y))              #store lowpoint pos
            Part1.append(heightmap[x][y])       #store low point value


print("Part1: ",sum(Part1)+len(Part1))      #sum of low points + size of low points = risk factor 

basin = []
for lp in lowPoint:     #store basin size of lowpoints 
    x,y = lp
    basin.append(len(getbasin(x,y,maxX,maxY,heightmap)))

basin.sort()            #sort from small to big
basin.reverse()         #reverse order
Part2 = 1
for i in range(3):      #multiply 3 bigist basin 
    Part2 *= basin[i]

print("Part2: ",Part2)  #print Part2
