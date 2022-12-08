if __name__ == '__main__':
    print('Advent of Code 2022 - Day 03')

    with open('day03.txt') as f:
        rucksacks = [line for line in f.read().splitlines()]

    def get_priority(char: str) -> int:
        return ord(char) - 96 if char.islower() else ord(char) - 38


    # part 1

    total_priorities1 = 0
    for rucksack in rucksacks:
        compartment_length = len(rucksack)//2
        first_compartment = rucksack[:compartment_length]

        for char in rucksack[compartment_length:]:
            if char in first_compartment:
                total_priorities1 += get_priority(char)
                break
        else:
            continue


    print(f'Part 1: {total_priorities1}') # 8039


    # part 2

    groups = [rucksacks[i:i+3] for i in range(0,len(rucksacks),3)]
    total_priorities2 = 0

    for group in groups:
        elf1, elf2, elf3 = group
        badge = set(elf1).intersection(set(elf2)).intersection(set(elf3))
        total_priorities2 += get_priority(badge.pop())


    print(f'Part 2: {total_priorities2}') # 2510
