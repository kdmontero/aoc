from collections import Counter

print("Advent of Code 2017 - Day 04: High-Entropy Passphrases")
with open('day04.txt') as f:
    phrases = [line.split(' ') for line in f.read().splitlines()]

# part 1
valid1 = 0
valid1_pp = []
for pp in phrases:
    if len(set(pp)) == len(pp):
        valid1 += 1
        valid1_pp.append(pp)

print(f'Part 1: {valid1}') # 325


# part 2
valid2 = 0
for pp in valid1_pp:
    counters = []
    for word in pp:
        if Counter(word) in counters:
            break
        counters.append(Counter(word))
    else:
        valid2 += 1

print(f'Part 2: {valid2}') # 119
