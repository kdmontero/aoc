from functools import lru_cache


if __name__ == '__main__':
    print("Advent of Code 2024 - Day 19: Linen Layout")

    with open('day19.txt') as f:
        raw_patterns, raw_towels = f.read().strip().split('\n\n')
        patterns = raw_patterns.split(', ')
        towels = raw_towels.splitlines()


    # part 1

    @lru_cache
    def is_possible(towel: str) -> bool:
        if towel == '':
            return True

        for pattern in patterns:
            if towel.startswith(pattern):
                if is_possible(towel.removeprefix(pattern)):
                    return True
        else:
            return False

    possible_towels = []
    for towel in towels:
        if is_possible(towel):
            possible_towels.append(towel)

    print(f'Part 1: {len(possible_towels)}') # 330


    # part 2

    @lru_cache
    def check(towel: str, count: int) -> int:
        if towel == '':
            return count + 1

        for pattern in patterns:
            if towel.startswith(pattern):
                count += check(towel.removeprefix(pattern), 0)
        return count

    possible_ways = 0
    for towel in possible_towels:
        possible_ways += check(towel, 0)

    print(f'Part 2: {possible_ways}') # 950763269786650

