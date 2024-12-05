from __future__ import annotations


class Page:
    def __init__(self, val: str) -> None:
        self.val = int(val)
        self.high_side = set() # pages that has higher order than self
        self.low_side = set() # pages that has lower order than self

    def __lt__(self, other: Page) -> bool:
        return self.val in other.low_side
        

if __name__ == '__main__':
    print('Advent of Code 2024 - Day 05')

    with open('day05.txt') as f:
        rules, raw_updates = f.read().split('\n\n')

        pages = {}
        for rule in rules.splitlines():
            low, high = [int(page) for page in rule.split('|')]

            if low not in pages:
                pages[low] = Page(low)
            pages[low].high_side.add(high)

            if high not in pages:
                pages[high] = Page(high)
            pages[high].low_side.add(low)

        updates = []
        for line in raw_updates.splitlines():
            update = [pages[int(p)] for p in line.split(',')]
            updates.append(update)


    valid_mid_page_sum = 0
    invalid_mid_page_sum = 0

    for update in updates:
        sorted_update = sorted(update[:])
        if sorted_update == update:
            valid_mid_page_sum += update[len(update)//2].val
        else:
            invalid_mid_page_sum += sorted_update[len(update)//2].val


    print(f'Part 1: {valid_mid_page_sum}') # 7074

    print(f'Part 2: {invalid_mid_page_sum}') # 4828

