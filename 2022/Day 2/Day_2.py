
rounds = []

# 1 for Rock, 2 for Paper, and 3 for Scissors
# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.

for i in open("Day-2-input.txt").read().split("\n"):
    shapes = i.split(" ")
    points = []
    if shapes[0] == "A":
        points.append(1)
    elif shapes[0] == "B":
        points.append(2)
    elif shapes[0] == "C":
        points.append(3)

    if shapes[1] == "X":
        points.append(1)
    elif shapes[1] == "Y":
        points.append(2)
    elif shapes[1] == "Z":
        points.append(3)

    rounds.append(points);


#0 if you lost, 3 if the round was a draw, and 6 if you won
points = 0

for i in rounds:
    points += i[1]

    if i[0] == i[1]:
        points += 3
    elif i[0] == i[1]-1 or i[0] == i[1]+2:
        points += 6
    else:
        points += 0

print("Part 1: ", points)
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

points = 0

for i in rounds:

    if i[1] == 1:
        points += 0

        if i[0] == 3:
            points += 2
        elif i[0] == 2:
            points += 1
        else:
            points += 3
    
    elif i[1] == 2:
        points += 3
        points += i[0]
    
    else:
        points += 6

        if i[0] == 3:
            points += 1
        elif i[0] == 2:
            points += 3
        else:
            points += 2

print("Part 2: ", points)
