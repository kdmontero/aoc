print('Advent of Code 2015 - Day 16')
with open('day16.txt') as f:
    aunts = []
    for line in f.read().splitlines():
        line = line.replace(':','').replace(',','').replace('Sue', 'id').split(' ')
        data = {}
        for i in range(1, len(line), 2):
            data[line[i-1]] = int(line[i])
        aunts.append(data)

MFCSAM = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''

real_sue = {}
for prop in MFCSAM.splitlines():
    key, value = prop.split(': ')
    real_sue[key] = int(value)

# part 1
for aunt in aunts:
    for prop in real_sue.keys():
        if aunt.get(prop) is None:
            continue
        if aunt[prop] != real_sue[prop]:
            break
    else:
        correct_aunt1 = aunt['id']
        break

print(f'Part 1: {correct_aunt1}') # 373


# part 2
for aunt in aunts:
    for prop in real_sue.keys():
        if aunt.get(prop) is None:
            continue
        if prop in {'cats', 'trees'}:
            if aunt[prop] <= real_sue[prop]:
                break
        elif prop in {'pomeranians', 'goldfish'}:
            if aunt[prop] >= real_sue[prop]:
                break 
        else:
            if aunt[prop] != real_sue[prop]:
                break
    else:
        correct_aunt2 = aunt['id']
        break

print(f'Part 2: {correct_aunt2}') # 260
