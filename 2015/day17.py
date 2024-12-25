import collections

print("Advent of Code 2015 - Day 17: No Such Thing as Too Much")
with open('day17.txt') as f:
    containers = sorted([int(i) for i in f.read().splitlines()])

REFRIGERATOR = 150
counter = collections.Counter()

def count_containers(target, addends, remaining):
    if target == 0:
        counter[len(addends)] += 1
        return 1
    elif target < 0:
        return 'Invalid'
    else:
        total = 0
        for i, cont in enumerate(remaining):
            count = count_containers(target-cont, addends+[cont], remaining[i+1:])
            if count == 'Invalid':
                break
            total += count    
        return total

# part 1
print(f'Part 1: {count_containers(REFRIGERATOR, [], containers)}') # 1304


# part 2
min_addends = min(counter.keys(), key=counter.get)
print(f'Part 2: {counter[min_addends]}') # 18
