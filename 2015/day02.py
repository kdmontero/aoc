print('Advent of Code 2015 - Day 02')
with open('day02.txt') as f:
    gifts = [[int(i) for i in gift.split('x')] 
        for gift in f.read().splitlines()]

# part 1
area = 0
for gift in gifts:
    l, w, h = gift
    area += 2 * ((l*w) + (w*h) + (l*h))
    if max(gift) == l:
        area += w*h
    elif max(gift) == w:
        area += l*h
    elif max(gift) == h:
        area += w*l

print(f'Part 1: {area}') # 1588178


# part 2
length = 0
for gift in gifts:
    l, w, h = gift
    length += l * w * h
    if max(gift) == l:
        length += 2 * (w + h)
    elif max(gift) == w:
        length += 2 * (l + h)
    elif max(gift) == h:
        length += 2 * (w + l)

print(f'Part 2: {length}') # 3783758
