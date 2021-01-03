with open('day12.txt') as f:
    doc = f.read().strip()

# part 1
i = 0
cont = False
total = 0
while i < len(doc):
    if not cont:
        if doc[i].isdigit():
            if doc[i-1] == '-':
                current = '-' + doc[i]
            else:
                current = doc[i]
            cont = True
    else:
        if doc[i].isdigit():
            current += doc[i]
        else:
            total += int(current)
            cont = False
    i += 1

print(f'Part 1: {total}') # 111754