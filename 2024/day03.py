import re


if __name__ == '__main__':
    print('Advent of Code 2024 - Day 03')

    with open('day03.txt') as f:
        program = f.read().splitlines()


    # part 1

    pattern1 = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

    result1 = 0
    for line in program:
        for num1, num2 in pattern1.findall(line):
            result1 += int(num1) * int(num2)

    print(f'Part 1: {result1}') # 188741603


    # part 2

    pattern2 = re.compile(r"(don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\))")

    result2 = 0
    do_flag = True
    for line in program:
        for instruction in pattern2.findall(line):
            if do_flag and instruction == "don't()":
                do_flag = False
                continue
            if not do_flag and instruction == "do()":
                do_flag = True
                continue
            if do_flag and instruction not in {"do()", "don't()"}:
                num1, num2 = pattern1.findall(instruction)[0]
                result2 += int(num1) * int(num2)

    print(f'Part 2: {result2}') # 67269798

