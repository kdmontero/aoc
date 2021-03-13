import collections

print('Advent of Code 2017 - Day 07')
with open('day07.txt') as f:
    base_program = {}
    weights = {}
    subprogram = {}

    for line in f.read().splitlines():
        line = line.replace('(', '').replace(')', '')
        if '->' in line:
            main, subtowers = line.split(' -> ')
            name, weight = main.split(' ')
            subtowers = subtowers.split(', ')
            subprogram[name] = subtowers

            for program in subtowers:
                base_program[program] = name

        else:
            name, weight = line.split(' ')

        weights[name] = int(weight)


# part 1
bottom = list(base_program.keys())[0]

while base_program.get(bottom):
    bottom = base_program[bottom]

print(f'Part 1: {bottom}') # cyrupz


# part 2
total_weights = {}

def find_program_weight(program):
    if program in total_weights:
        return total_weights[program]

    total_weight = weights[program]

    if program not in subprogram:
        total_weights[program] = total_weight
        return total_weight

    for sub in subprogram[program]:
        total_weight += find_program_weight(sub)

    total_weights[program] = total_weight
    return total_weight

queue = [(bottom, None)]
while queue:
    node, target = queue.pop()
    subprogram_weights = []
    subprograms = []

    for sub in subprogram[node]:
        subprograms.append(sub)
        subprogram_weights.append(find_program_weight(sub))

    tally = collections.Counter(subprogram_weights)
    if len(tally) == 1:
        correct_weight = target - sum(subprogram_weights)
        break

    if len(subprograms) > 2:
        subtarget = max(tally, key=tally.get)
        wrong_weight = min(tally, key=tally.get)
        unbalanced = subprograms[subprogram_weights.index(wrong_weight)]
        queue.append((unbalanced, subtarget))

    elif len(subprograms) == 2:
        for sub, sub_weight in zip(subprograms, subprogram_weights):
            subtarget = (target - weight[node]) / 2
            if sub_weight != subtarget:
                queue.append((sub, subtarget))

print(f'Part 2: {correct_weight}') # 193
