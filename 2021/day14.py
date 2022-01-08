import collections

if __name__ == '__main__':
    print('Advent of Code 2021 - Day 14')

    with open('day14.txt') as f:
        template, raw_rules = f.read().split('\n\n')
        rules = {}

        for line in raw_rules.splitlines():
            pair, inserted = line.split(' -> ')
            rules[pair] = [pair[0] + inserted, inserted + pair[1]]


    def expand(polymer, steps):
        start, end = polymer[0], polymer[-1]
        pair_count = collections.Counter()

        for i in range(len(polymer) -1):
            pair = polymer[i] + polymer[i+1]
            pair_count[pair] += 1

        for _ in range(steps):
            new_count = collections.Counter()
            for pair, count in pair_count.items():
                for result_pair in rules[pair]:
                    new_count[result_pair] += count
            pair_count = new_count

        char_count = collections.Counter()
        char_count[start] = 1
        char_count[end] = 1
        for pair, count in pair_count.items():
            char_count[pair[0]] += count
            char_count[pair[1]] += count

        quantities = sorted(char_count.values())

        return (quantities[-1] - quantities[0]) // 2


    print(f'Part 1: {expand(template, 10)}') # 2621 - part 1

    print(f'Part 2: {expand(template, 40)}') # 2843834241366 - part 2
