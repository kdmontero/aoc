if __name__ == '__main__':
    print('Advent of Code 2017 - Day 19')

    with open('day19.txt') as f:
        diagram = {}
        
        for y, lines in enumerate(f.read().splitlines()):
            for x, char in enumerate(lines):
                if char != ' ':
                    diagram[(y,x)] = char

        for y, x in diagram:
            if y == 0:
                pointer = (y, x)
                direction = 'DOWN'
                break
        
    def move(pointer, direction):
        y, x = pointer
        if direction == 'DOWN':
            return (y+1, x)
        elif direction == 'UP':
            return (y-1, x)
        elif direction == 'RIGHT':
            return (y, x+1)
        elif direction == 'LEFT':
            return (y, x-1)

    def turn(char, direction, pointer):
        y, x = pointer
        if direction in ['DOWN', 'UP'] and char == '+':
            if diagram.get((y, x+1)) not in ['|', None]:
                return 'RIGHT'
            elif diagram.get((y, x-1)) not in ['|', None]:
                return 'LEFT'
        elif direction in ['LEFT', 'RIGHT'] and char == '+':
            if diagram.get((y+1, x)) not in ['-', None]:
                return 'DOWN'
            elif diagram.get((y-1, x)) not in ['-', None]:
                return 'UP'
        return direction


    letters = ''
    steps = 1
    while True:
        pointer = move(pointer, direction)
        char = diagram.get(pointer)
        if char == None:
            break

        steps += 1
        if char not in ['|', '-', '+']:
            letters += char

        direction = turn(char, direction, pointer)

    print(f'Part 1: {letters}') # YOHREPXWN - part 1
    print(f'Part 2: {steps}') # 16734 - part 2
