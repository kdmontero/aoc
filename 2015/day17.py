import collections

with open('day17.txt') as f:
    containers = sorted([int(i) for i in f.read().splitlines()])

REFRIGERATOR = 150
counter = collections.Counter()

def count_containers(size, addends, liters):
    if size == 0:
        counter[len(addends)] += 1
        return 1
    elif size < 0:
        return 'Invalid'
    else:
        total = 0
        for i, cont in enumerate(liters):
            count = count_containers(size-cont, addends+[cont], liters[i+1:])
            if count == 'Invalid':
                addends.pop()
                break
            total += count    
        return total

# part 1
print(f'Part 1: {count_containers(REFRIGERATOR, [], containers)}') # 1304


# part 2
min_addends = min(counter.keys(), key=counter.get)
print(f'Part 2: {counter[min_addends]}') # 18