import collections

with open('day24.txt') as f:
    layout = set()
    for y, line in enumerate(f.read().splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                layout.add((y, x))

# part 1
seen = []
while layout not in seen:
    seen.append(layout)
    checker = collections.Counter()
    for y, x in layout:
        checker[(y+1, x)] += 1
        checker[(y-1, x)] += 1
        checker[(y, x+1)] += 1
        checker[(y, x-1)] += 1

    new_layout = set()
    for y in range(5):
        for x in range(5):
            if any([
                (y, x) in layout and checker[(y, x)] == 1, 
                (y, x) not in layout and checker[(y, x)] in {1, 2}
            ]):
                new_layout.add((y, x))

    if new_layout in seen:
        break
    else:
        layout = new_layout

biodiversity = 0
for y, x in new_layout:
    biodiversity += 2**(y*5 + x)

print(f'Part 1: {biodiversity}') # 18859569