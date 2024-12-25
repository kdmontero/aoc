import collections
import math

print("Advent of Code 2015 - Day 24: It Hangs in the Balance")
with open('day24.txt') as f:
    packages = sorted([int(i) for i in f.read().splitlines()])

def valid_group(target, addends, remaining):
    global smallest_capacity, min_QE

    if target == 0:
        if len(addends) < smallest_capacity:
            smallest_capacity = len(addends)
            min_QE = math.prod(packages)

        if len(addends) == smallest_capacity:
            min_QE = min(min_QE, math.prod(addends))

        return 1
    
    elif len(addends) > smallest_capacity or target < 0:
        return 'Invalid'

    else:
        total = 0
        for i, cont in enumerate(remaining):
            count = valid_group(target-cont, addends+[cont], remaining[i+1:])
            if count == 'Invalid':
                break
            total += count
        return total


# part 1
target_weight1 = sum(packages) // 3
smallest_capacity = len(packages)
min_QE = math.prod(packages)
valid_group(target_weight1, [], packages)

print(f'Part 1: {min_QE}') # 11846773891


# part 2
target_weight2 = sum(packages) // 4
smallest_capacity = len(packages)
min_QE = math.prod(packages)
valid_group(target_weight2, [], packages)

print(f'Part 2: {min_QE}') # 80393059
