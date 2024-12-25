if __name__ == '__main__':
    print("Advent of Code 2022 - Day 01: Calorie Counting")

    with open('day01.txt') as f:
        elves = []

        for group in f.read().split('\n\n'):
            elves.append(group)

    calories_list = []

    for elf in elves:
        cal = 0
        for food in elf.splitlines():
            cal += int(food)

        calories_list.append(cal)

    calories_list.sort(reverse=True)

    print(f'Part 1: {calories_list[0]}') # 69795 - part 1


    print(f'Part 2: {sum(calories_list[0:3])}') # 208437 - part 2
