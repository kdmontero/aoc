from itertools import combinations

if __name__ == '__main__':
    print("Advent of Code 2025 - Day 05: Cafeteria")

    Range = tuple[int, int]

    with open('day05.txt') as f:
        raw_ranges, raw_ids = f.read().strip().split('\n\n')

        ranges: list[Range] = []
        for range_ in raw_ranges.splitlines():
            low, high = range_.split('-')
            ranges.append((int(low), int(high)))

        ids: list[int] = [int(id_) for id_ in raw_ids.splitlines()]

    # part 1

    def check_id(id_: int) -> bool:
        for low, high in ranges:
            if low <= id_ <= high:
                return True
        return False

    fresh = sum(check_id(id_) for id_ in ids)

    print(f'Part 1: {fresh}') # 701


    # part 2

    def compare_ranges(
        low1: int, high1: int, low2: int, high2: int
    ) -> tuple[int, int] | tuple[int, int, int, int]:

        # Case A: there is no overlap, w/ space in between (range 1 < range 2)
        # 1   -------
        # 2            -------
        if low2 - high1 > 1:
            return (low1, high1, low2, high2)

        # Case B: there is no overlap, w/ space in between (range 2 < range 1)
        # 1            -------
        # 2   -------
        if low1 - high2 > 1:
            return (low2, high2, low1, high1)

        # Case C: there is no overlap, w/o space in between (range 1 < range 2)
        # 1   -------
        # 2          -------
        elif (low1 <= high1 < low2 <= high2) and low2 - high1 == 1:
            return (low1, high2)

        # Case D: there is no overlap, w/o space in between (range 2 < range 1)
        # 1          -------
        # 2   -------
        elif (low2 <= high2 < low1 <= high1) and low1 - high2 == 1:
            return (low2, high1)
        
        # Case E: range 1 completely overlaps range 2
        # 1   ----------
        # 2       -----
        elif low1 <= low2 <= high2 <= high1:
            return (low1, high1)

        # Case F: range 2 completely overlaps range 1
        # 1   ------
        # 2   -----------
        elif low2 <= low1 <= high1 <= high2:
            return (low2, high2)

        # Case G: there is a partial overlap (range 1 < range 2)
        # 1   -------
        # 2      -------
        elif low1 <= low2 <= high1 <= high2:
            return (low1, high2)

        # Case H: there is a partial overlap (range 2 < range 1)
        # 1      -------
        # 2   -------
        elif low2 <= low1 <= high2 <= high1:
            return (low2, high1)
        
        else:
            raise NotImplementedError(f'{low1}-{high1}, {low2}-{high2}')


    ranges.sort(key=lambda a: a[0])
    organized_ranges: list[Range] = [ranges[0]]

    for range_ in ranges[1:]:
        low1, high1 = range_
        low2, high2 = organized_ranges.pop()

        results = compare_ranges(low1, high1, low2, high2)

        if len(results) == 2:
            organized_ranges.append(results)
        elif len(results) == 4:
            new_low1, new_high1, new_low2, new_high2 = results
            organized_ranges.append((new_low1, new_high1))
            organized_ranges.append((new_low2, new_high2))

    all_fresh = 0
    for low, high in organized_ranges:
        all_fresh += high - low + 1

    print(f'Part 2: {all_fresh}') # 352340558684863

