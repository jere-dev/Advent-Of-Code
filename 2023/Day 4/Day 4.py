lines = open("puzzle-input.txt").read().splitlines()

winning = [line.split("|")[0].split()[2::] for line in lines]
cards = [line.split("|")[1].split() for line in lines]

def recCopy(cardNum, numOfCopy, d):
    for c in range(numOfCopy):
        d[cardNum+c+1] = d.get(cardNum+c+1, 1) + 1
    return d

answer = 0
d = {}
for card in range(len(cards)):
    point = 0
    matchNum = 0
    if card+1 not in d:
        d[card+1] = 1
    for num in cards[card]:
        if num in winning[card]:
            matchNum += 1
            if point == 0:
                point = 1
            else:
                point *= 2
    for i in range(d.get(card, 1)):
        d = recCopy(card, matchNum, d)

    answer += point

print("Part 1: ", answer)

answer = 0
for k in d:
    answer += d[k]

print("Part 2: ", answer) 