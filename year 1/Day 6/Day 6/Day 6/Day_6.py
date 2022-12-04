def count_fish(fishs,days):
    #store fish states eg 0 fish 1 fish 2 fish 3 fish
    fish_states = []
    for i in range(9):
        fish_states.append(fishs.count(i))
    #add spawns 7 days out
    for day in range(days):
        fish_states[(day + 7) % 9] += fish_states[day % 9]

    #return num of fishes
    return sum(fish_states)


# test input input = [3,4,3,1,2]
#open input file and store 
input = []
for num in open("../../Day-6-input.txt").read().strip().split(","):
    input.append(int(num))


print("Part1: ",count_fish(input,80))
print("Part2: ",count_fish(input,256))