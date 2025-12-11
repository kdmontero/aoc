if __name__ == '__main__':
    print("Advent of Code 2025 - Day 02: Gift Shop")

    with open('day02.txt') as f:
        ranges: list[tuple[int, int]] = []
        for range_ in f.read().strip().split(','):
            low, high = range_.split('-')
            ranges.append((int(low), int(high)))

    # part 1

    def is_invalid1(num: str) -> bool:
        repeat_len, remainder = divmod(len(str(num)), 2)
        if remainder != 0:
            return False

        for digit in range(repeat_len + 1):
            char = num[digit]
            for other_digit in range(digit, len(num), repeat_len):
                if num[other_digit] != char:
                    break
            else:
                continue
            break
        else:
            return True
        return False

    invalid_ids1 = 0
    for low, high in ranges:
        for num in range(low, high + 1):
            if is_invalid1(str(num)):
                invalid_ids1 += num

    print(f'Part 1: {invalid_ids1}') # 12599655151


    # part 2

    def is_invalid2(num: str) -> bool:
        for repeat_len in range(1, len(num)):
            if len(num) % repeat_len != 0:
                continue

            for digit in range(repeat_len + 1):
                char = num[digit]
                for other_digit in range(digit, len(num), repeat_len):
                    if num[other_digit] != char:
                        break
                else:
                    continue
                break
            else:
                return True
        else:
            return False

    invalid_ids2 = 0
    for low, high in ranges:
        for num in range(low, high + 1):
            if is_invalid2(str(num)):
                invalid_ids2 += num

    print(f'Part 2: {invalid_ids2}') # 20942028255

