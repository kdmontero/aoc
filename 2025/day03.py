if __name__ == '__main__':
    print("Advent of Code 2025 - Day 03: Lobby")

    with open('day03.txt') as f:
        banks = f.read().strip().splitlines()

    def get_joltage(bank: str, *, length: int) -> str:
        max_batt = max(bank[:len(bank) - length + 1])
        batt_index = bank.index(max_batt)

        if length == 1:
            return max_batt

        return max_batt + get_joltage(bank[batt_index + 1:], length=length - 1)

    total_joltage1 = 0
    total_joltage2 = 0

    for bank in banks:
        total_joltage1 += int(get_joltage(bank, length=2))
        total_joltage2 += int(get_joltage(bank, length=12))

    print(f'Part 1: {total_joltage1}') # 17343

    print(f'Part 2: {total_joltage2}') # 172664333119298

