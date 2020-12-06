with open('day06.txt') as f:
    data = [
        [set(individual) for individual in group.split('\n')] 
        for group in f.read().split('\n\n')
    ]

total1 = total2 = 0
for group in data:
    total1 += len(set.union(*group))
    total2 += len(set.intersection(*group))

print(total1) # 6161 - part 1
print(total2) # 2971 - part 2