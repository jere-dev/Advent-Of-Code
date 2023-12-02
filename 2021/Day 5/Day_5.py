Part1 = {}
Part2 = {}

for line in open('Day-5-input.txt'):
    first,last = line.split('->')
    x1,y1 = first.split(',')
    x2,y2 = last.split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if x1==x2:
        if y1>y2: 
            y1,y2=y2,y1
        for y in range(y1,y2+1):
          Part1[(x1,y)]=Part1.get((x1,y),0)+1
          Part2[(x1,y)]=Part2.get((x1,y),0)+1
    elif y1==y2:
        if x1>x2: 
            x1,x2=x2,x1
        for x in range(x1,x2+1):
          Part1[(x,y1)]=Part1.get((x,y1),0)+1
          Part2[(x,y1)]=Part2.get((x,y1),0)+1
    else:
        if x1>x2: 
            x1,x2, y1,y2 = x2,x1, y2,y1
        for x in range(x1,x2+1):
          if y2>y1: 
              y = y1+(x-x1)
          else:     
              y = y1-(x-x1)
          Part2[(x,y)]=Part2.get((x,y),0)+1

ans1 = 0
for k in Part1:
    if Part1[k] > 1:
        ans1 += 1

ans2 = 0
for k in Part2:
    if Part2[k] > 1:
        ans2 += 1

print("Part1: ",ans1)
print("Part2: ",ans2)
