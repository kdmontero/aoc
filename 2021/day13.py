if __name__ == '__main__':
    print('Advent of Code 2021 - Day 13')

    with open('day13.txt') as f:
        dots = set()
        ins = []
        dot_list, instructions = f.read().split('\n\n')

        for dot in dot_list.split('\n'):
            x, y = dot.split(',')
            dots.add((int(x), int(y)))

        for instruction in instructions.split('\n'):
            _, _, i = instruction.split()
            direction, value = i.split('=')
            ins.append([direction, int(value)])

    
    # part 1

    def fold(dots, ins):
        line, fold_line = ins
        new_dots = set()
        
        for dot in dots:
            x, y = dot
            if line == 'x' and x > fold_line:
                offset = x - fold_line
                new_dots.add((fold_line - offset, y))

            elif line == 'y' and y > fold_line:
                offset = y - fold_line
                new_dots.add((x, fold_line - offset))

            else:
                new_dots.add((x, y))

        return new_dots

    print(f'Part 1: {len(fold(dots, ins[0]))}') # 664


    # part 2

    EMPTY = ' '
    DOT = '#'

    def print_dots(dots):
        min_x, min_y, max_x, max_y = 999_999_999, 999_999_999, 0, 0

        for dot in dots:
            x, y = dot
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        x_offset, y_offset = min_x, min_y
        paper = [[EMPTY] * (max_x - min_x + 1) for _ in range(min_y, max_y + 1)]

        for dot in dots:
            x, y = dot
            paper[y - y_offset][x - x_offset] = DOT

        for line in paper:
            print(''.join(line))

    
    for i in ins:
        dots = fold(dots, i)

    print(f'Part 2: ') # EFJKZLBL
    print_dots(dots)
