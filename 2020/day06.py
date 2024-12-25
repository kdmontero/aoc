print("Advent of Code 2020 - Day 06: Custom Customs")
with open('day06.txt') as f:
    data = [
        [set(individual) for individual in group.split('\n')] 
        for group in f.read().split('\n\n')
    ]

total1 = total2 = 0
for group in data:
    total1 += len(set.union(*group))
    total2 += len(set.intersection(*group))

print(f'Part 1: {total1}') # 6161 - part 1

print(f'Part 2: {total2}') # 2971 - part 2
