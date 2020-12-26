with open('day01.txt') as f:
    directions = f.read()

floor = 0
found = False
for i, p in enumerate(directions):
    if p == '(':
        floor += 1
    elif p == ')':
        floor -= 1
    if floor == -1 and not found:
        position = i + 1
        found = True

print(f'Part 1: {floor}') # 280
print(f'Part 2: {position}') # 1797