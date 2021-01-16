with open('day19.txt') as f:
    given_rep, medicine = f.read().split('\n\n')
    replacements = []
    for replacement in given_rep.strip().splitlines():
        replacements.append(replacement.split(' => '))

# part 1
molecules = set()
for orig, new in replacements:
    count = medicine.count(orig)
    length = len(orig)
    replaced = 0
    start = 0
    while replaced != count:
        for i in range(start, len(medicine)-length+1):
            if medicine[i:i+length] == orig:
                molecules.add(medicine[:i] + new + medicine[i+length:])
                replaced += 1
                start = i + 1
                break

print(f'Part 1: {len(molecules)}') # 535