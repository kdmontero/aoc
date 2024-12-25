print("Advent of Code 2017 - Day 05: A Maze of Twisty Trampolines, All Alike")
with open('day05.txt') as f:
    offsets = [int(num) for num in f.read().splitlines()]

# part 1
i = jumps1 = 0
offsets1 = offsets[:]
try:
    while True:
        offsets1[i], i = offsets1[i] + 1, i + offsets1[i] # tuple order matters!
        jumps1 += 1
except IndexError:
    print(f'Part 1: {jumps1}') # 378980


# part 2
i = jumps2 = 0
offsets2 = offsets[:]
try:
    while True:
        if offsets2[i] >= 3:
            offsets2[i], i = offsets2[i] - 1, i + offsets2[i]
        else:
            offsets2[i], i = offsets2[i] + 1, i + offsets2[i]
        jumps2 += 1
except IndexError:
    print(f'Part 2: {jumps2}') # 26889114
