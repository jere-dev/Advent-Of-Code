
elfCal = []
for i in open("Day-1-input.txt").read().split("\n\n"):
    cal = 0
    for j in i.split():
        num = int(j)
        cal += num

    elfCal.append(cal)

elfCal.sort()
elfCal.reverse()
print("caleroies caried by the elf carying most calories: ",elfCal[0])
print("caleroies caried by the top three elf's carying most calories: ",elfCal[0] + elfCal[1] + elfCal[2])