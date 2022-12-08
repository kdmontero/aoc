if __name__ == '__main__':
    print('Advent of Code 2022 - Day 04')

    with open('day04.txt') as f:
        data = []
        for line in f.read().splitlines():
            pair_data = []
            for num in line.replace(',', '-').split('-'):
                pair_data.append(int(num))

            data.append(pair_data)
        
    total_count1 = 0
    total_count2 = 0

    for pair in data:
        elf1 = set(range(pair[0], pair[1] + 1))
        elf2 = set(range(pair[2], pair[3] + 1))

        if elf1.issubset(elf2) or elf2.issubset(elf1):
            total_count1 += 1

        if (elf1 & elf2):
            total_count2 += 1

    print(f'Part 1: {total_count1}') # 507 - part 1

    print(f'Part 2: {total_count2}') # 897 - part 2
