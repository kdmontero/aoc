import collections
from functools import lru_cache

if __name__ == '__main__':
    print('Advent of Code 2021 - Day 14')

    with open('day14.txt') as f:
        template, raw_rules = f.read().split('\n\n')
        rules = {}

        for line in raw_rules.splitlines():
            pair, inserted = line.split(' -> ')
            rules[pair] = pair[0] + inserted + pair[1]

    # part 1

    def expand(polymer):
        if len(polymer) == 2:
            return rules.get(polymer, polymer)
 
        else:
            half = (len(polymer) + 1)//2
            return expand(polymer[:half]) + expand(polymer[half-1:])[1:]

    def polymerize(polymer, steps):
        if steps == 1:
            return expand(polymer)
        else:
            return polymerize(expand(polymer), steps - 1)


    polymer = polymerize(template, 10)
    polymer_qty = collections.Counter(polymer)
    max_p, min_p = max(polymer_qty.values()), min(polymer_qty.values())

    print(f'Part 1: {max_p - min_p}') # 2621
