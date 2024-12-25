from itertools import cycle

print("Advent of Code 2018 - Day 01: Chronal Calibration")
with open('day01.txt') as f:
    sequence = f.read().splitlines()

# part 1
frequency1 = 0
for freq in sequence:
    if freq[0] == '+':
        frequency1 += int(freq[1:])
    elif freq[0] == '-':
        frequency1 -= int(freq[1:])

print(f'Part 1: {frequency1}') # 490


# part 2
frequency2 = 0
sequence = cycle(sequence)
seen = {0}
for freq in sequence:
    if freq[0] == '+':
        frequency2 += int(freq[1:])
    elif freq[0] == '-':
        frequency2 -= int(freq[1:])
    if frequency2 in seen:
        break
    seen.add(frequency2)

print(f'Part 2: {frequency2}') # 70357
