#store output letters from file in ouput 
output = []
signelpaterns = []
for n in open('../../Day-8-input.txt').read().split("|"):
    signelpaterns.append(n.split("\n"))
    output.append((n.split("\n")[0]))
output.remove(output[0])

#split each output line by space and store l in Part1
Part1 = []
for i in output:
    l = []
    for j in i.split(" "):
        l.append(j)
    l.remove(l[0])
    Part1.append(l)

#if j is unique increse NumOfUnique by 1
NumOfUnique = 0
OutputValue = 0
for i in Part1:
    ov = ""
    for j in i:
        if (len(j) == 2):                                                                      #1
            NumOfUnique += 1
            ov = ov +  "1"
        elif (len(j) == 4):                                                                    #4   
           NumOfUnique += 1
           ov = ov +  "4"
        elif (len(j) == 3):                                                                    #7
            NumOfUnique += 1
            ov = ov +  "7"
        elif (len(j) == 7):                                                                    #8
            NumOfUnique += 1
            ov = ov +  "8"
        elif 'c' in j and 'a' in j and 'g' in j and 'e' in j and 'd' in j and 'b' in j:        #0
            ov = ov +  "0"

        elif 'c' in j and 'd' in j and 'f' in j and 'g' in j and 'e' in j and 'b' in j:        #6
            ov = ov +  "6"
            #-----------------------------------------------------

        elif 'c' in j and 'd' in j and 'f' in j and 'b' in j and 'e' in j:                     #5
            ov = ov +  "5"

        elif 'g' in j and 'c' in j and 'd' in j and 'f' in j and 'a' in j:                     #2
            ov = ov +  "2"

        elif 'f' in j and 'b' in j and 'c' in j and 'a' in j and 'd' in j:                     #3
            ov = ov +  "3"

        elif 'c' in j and 'e' in j and 'f' in j and 'a' in j and 'b' in j and 'd' in j:        #9
            ov = ov +  "9"
        else:
            ov = ov + "0"
    OutputValue += int(ov)

            
print(signelpaterns)
print("\n\n\n",Part1)
#print answer for Part1
print("Part1: ",NumOfUnique)
print("Part2: ",OutputValue)

#8065398945135837