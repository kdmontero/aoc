with open('day06.txt') as f:
    memory = [int(num) for num in f.read().split()]

seen = set()
states = {}
steps = 0

def allocate(banks, index):
    blocks = banks[index]
    banks[index] = 0
    while blocks:
        index += 1
        if index == len(banks):
            index = 0
        banks[index] += 1
        blocks -= 1
    return banks

def get_index(banks):
    index = value = 0
    for i, v in enumerate(banks):
        if v > value:
            index = i
            value = v
    return index

while tuple(memory) not in seen:
    seen.add(tuple(memory))
    states[tuple(memory)] = steps
    index = get_index(memory)
    memory = allocate(memory, index)
    steps += 1

loop_size = steps - states[tuple(memory)]

print(f'Part 1: {steps}') # 11137 - part 1
print(f'Part 2: {loop_size}') # 1037  - part 2
