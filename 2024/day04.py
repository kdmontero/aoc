import re


if __name__ == '__main__':
    print("Advent of Code 2024 - Day 04: Ceres Search")

    with open('day04.txt') as f:
        word_search = [line for line in f.read().splitlines()]

    height = len(word_search)
    width = len(word_search[0])


    # part 1

    ws_transposed = []
    for x in range(height):
        transposed_line = ''
        for y in range(height):
            transposed_line += word_search[y][x]
        ws_transposed.append(transposed_line)

    ws_right_diagonal = []
    diagonal_rows = height + width - 1
    for i in range(diagonal_rows):
        diagonal_line = ''
        if i < height:
            x = 0
            y = i
        else:
            x = i - height + 1
            y = height - 1

        while (y > -1) and (x < width):
            diagonal_line += word_search[y][x]
            y -= 1
            x += 1

        ws_right_diagonal.append(diagonal_line)

    ws_reversed = word_search[-1::-1]
    ws_left_diagonal = []
    for i in range(diagonal_rows):
        diagonal_line = ''
        if i < height:
            x = 0
            y = i
        else:
            x = i - height + 1
            y = height - 1

        while (y > -1) and (x < width):
            diagonal_line += ws_reversed[y][x]
            y -= 1
            x += 1

        ws_left_diagonal.append(diagonal_line)

    total1 = 0
    puzzle = word_search + ws_transposed + ws_right_diagonal + ws_left_diagonal
    for line in puzzle:
        total1 += line.count('XMAS') + line.count('SAMX')

    print(f'Part 1: {total1}') # 2599


    # part 2

    def is_x_mas(y: int, x: int) -> bool:
        if all([
            word_search[y-1][x-1] == 'S',
            word_search[y-1][x+1] == 'S',
            word_search[y+1][x+1] == 'M',
            word_search[y+1][x-1] == 'M',
        ]) or all([
            word_search[y-1][x-1] == 'M',
            word_search[y-1][x+1] == 'S',
            word_search[y+1][x+1] == 'S',
            word_search[y+1][x-1] == 'M',
        ]) or all([
            word_search[y-1][x-1] == 'M',
            word_search[y-1][x+1] == 'M',
            word_search[y+1][x+1] == 'S',
            word_search[y+1][x-1] == 'S',
        ]) or all([
            word_search[y-1][x-1] == 'S',
            word_search[y-1][x+1] == 'M',
            word_search[y+1][x+1] == 'M',
            word_search[y+1][x-1] == 'S',
        ]):
            return True
        return False

    total2 = 0
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if word_search[y][x] == 'A':
                total2 += is_x_mas(y, x)

    print(f'Part 2: {total2}') # 1948

