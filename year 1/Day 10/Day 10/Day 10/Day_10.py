navSubsystem = [line for line in open("..\..\Day-10-input.txt").read().split("\n")]
points = 0
autoPoints = []

for line in navSubsystem:
    size_before = len(line)
    size_after = ""
    autoPoint = 0
    while size_before != size_after:
        size_before = len(line)
        line = line.replace("()","").replace("[]","").replace("{}","").replace("<>","")     #replaces complete brackets exemple ((){[]}) -> ({})  -> () | loop ends
        size_after = len(line)                                                              #loop stops when cant replace any more 
    
    
    for char in range(len(line)):                                                           #find first closing symbol and add points accordingly 
        if line[char] == ')':
            points += 3
            break
        elif line[char] == ']':
            points += 57
            break
        elif line[char] == '}':
            points += 1197
            break
        elif line[char] == '>':
            points += 25137
            break       

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Part2
    
    if ")" not in line and "]" not in line and "}" not in line and ">" not in line:         #find incomplete lines
        for i in range(len(line)):                                                          #add points to autoPoint for brackets starting from end 
            i = len(line) - i -1
            if line[i] == "(":
                autoPoint = autoPoint * 5
                autoPoint += 1
            elif line[i] == "[":
                autoPoint = autoPoint * 5
                autoPoint += 2
            elif line[i] == "{":
                autoPoint = autoPoint * 5
                autoPoint += 3
            elif line[i] == "<":
                autoPoint = autoPoint * 5
                autoPoint += 4

    if autoPoint != 0:                                                                      #if autoPoint is not 0 add to autoPoints
        autoPoints.append(autoPoint)

autoPoints.sort()

print("Part1: ",points)
print("Part2: ",autoPoints[int(len(autoPoints)/2)])                                         #Part2 is middile of autoPoints