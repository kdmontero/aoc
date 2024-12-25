print("Advent of Code 2020 - Day 10: Adapter Array")
with open('day10.txt') as f:
    adapters = [int(i) for i in f.read().split('\n')]

adapters.sort()
device = adapters[-1] + 3
adapters = [0] + adapters + [device]

# part 1
jolts = {
    1: 0,
    2: 0,
    3: 0
}

for i in range(1, len(adapters)):
    diff = adapters[i] - adapters[i-1]
    jolts[diff] += 1

print(f'Part 1: {jolts[1] * jolts[3]}') # 2475


# part 2
paths = {0: 1}
adapters.pop(0)
for num in adapters:
    a = paths[num-1] if num-1 in paths else 0
    b = paths[num-2] if num-2 in paths else 0
    c = paths[num-3] if num-3 in paths else 0
    paths[num] = a + b + c

print(f'Part 2: {paths[device]}') # 442136281481216
