print('Advent of Code 2015 - Day 19')
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


# part 2 - found in reddit that greedy algorithm works for the specific input
# used backtracking

replacements.sort(key=lambda x: -len(x[1]))
def find_steps(medicine, target, steps):
    if medicine == target:
        return steps

    for orig, new in replacements:
        if new not in medicine:
            continue
        count = medicine.count(new)
        medicine = medicine.replace(new, orig)
        return count + find_steps(medicine, target, steps)

    return 0

print(f'Part 2: {find_steps(medicine, "e", 0)}') # 212