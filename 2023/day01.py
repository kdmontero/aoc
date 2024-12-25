if __name__ == '__main__':
    print("Advent of Code 2023 - Day 01: Trebuchet?!")

    with open('day01.txt') as f:
        document = [line for line in f.read().splitlines()]

    
    # part 1

    total1 = 0
    for line in document:
        calib_value = ''
        for char in line:
            if char.isdigit():
                calib_value += char
                break
        for char in line[::-1]:
            if char.isdigit():
                calib_value += char
                break
        total1 += int(calib_value)
        
    print(f'Part 1: {total1}') # 54632


    # part 2

    nums = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'zero',
    ]

    nums += [str(num) for num in range(10)]
    
    def find_value(string):
        
        word_to_digit = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0',
        }

        if len(string) > 1:
            return word_to_digit[string]
        return string

    def find_digits(line):
        char_before_first = 100
        char_after_last = 100
        first_digit = ''
        last_digit = ''

        for num in nums:
            first_chars = line.split(num)[0]
            last_chars = line.split(num)[-1]

            if len(first_chars) < char_before_first:
                char_before_first = len(first_chars)
                first_digit = find_value(num)

            if len(last_chars) < char_after_last:
                char_after_last = len(last_chars)
                last_digit = find_value(num)

        return int(first_digit + last_digit)

    total2 = 0
    for line in document:
        total2 += find_digits(line)

    print(f'Part 2: {total2}') # 54019
