import itertools

print("Advent of Code 2015 - Day 13: Knights of the Dinner Table")
with open('day13.txt') as f:
    notes = {}
    for line in f.read().splitlines():
        person_and_rate, other = line.rstrip('.').split(
            ' happiness units by sitting next to ')
        person, rate = person_and_rate.split(' would ')
        rate = rate.split(' ')
        if rate[0] == 'gain':
            rating = int(rate[1])
        elif rate[0] == 'lose':
            rating = -int(rate[1])
        if person not in notes:
            notes[person] = {other: rating}
        else:
            notes[person][other] = rating

def get_rating(person, other):
    if person in notes and other in notes:
        return notes.get(person).get(other)
    else: 
        return 0

def total_happiness(arrangement: list) -> int:
    start = first = arrangement.pop(0)
    happiness = 0
    while arrangement:
        beside = arrangement.pop(0)
        happiness += get_rating(start, beside)
        happiness += get_rating(beside, start)
        start = beside
    happiness += get_rating(start, first)
    happiness += get_rating(first, start)
    return happiness

# part 1
max_total1 = 0
for arrangement in itertools.permutations(notes.keys()):
    total = total_happiness(list(arrangement))
    max_total1 = max(max_total1, total)

print(f'Part 1: {max_total1}') # 709

# part 2
max_total2 = 0
for arrangement in itertools.permutations(notes.keys()):
    total = total_happiness(list(arrangement)+['ME'])
    max_total2 = max(max_total2, total)

print(f'Part 2: {max_total2}') # 668
