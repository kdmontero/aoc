if __name__ == '__main__':
    print("Advent of Code 2024 - Day 25: Code Chronicle")

    with open('day25.txt') as f:
        locks = []
        keys = []
        for obj in f.read().strip().split('\n\n'):
            if obj.startswith('#'):
                locks.append(obj.splitlines())
            else:
                keys.append(obj.splitlines())

    def does_fit(lock: list[str], key: list[str]) -> bool:
        for line_lock, line_key in zip(lock, key):
            for char_lock, char_key in zip(line_lock, line_key):
                if char_lock == '#' and char_key == '#':
                    return False
        return True

    fits = 0
    for lock in locks:
        for key in keys:
            fits += does_fit(lock, key)

    print(f'Part 1: {fits}') # 3451

    print(f'Part 2: Complete all 49 stars in Advent of Code 2024') #

