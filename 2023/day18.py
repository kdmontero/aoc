import re


if __name__ == '__main__':
    print('Advent of Code 2023 - Day 18')

    with open('day18.txt') as f:
        dig_plan1 = []
        dig_plan2 = []
        pattern = re.compile(r'([UDLR]) ([0-9]+) \(\#([0-9a-z]+)\)')
        for line in f.read().splitlines():
            direction1, num1, hexadecimal = pattern.findall(line)[0]
            dig_plan1.append([direction1, int(num1)])

            num2, direction2 = hexadecimal[:-1], hexadecimal[-1]
            dig_plan2.append([direction2, int(num2, 16)])
    
    def get_next_corner(y: int, x: int, way: str, seq: int) -> list[int, int]:
        if way in 'U3':
            return [y - seq, x]
        elif way in 'D1':
            return [y + seq, x]
        elif way in 'L2':
            return [y, x - seq]
        elif way in 'R0':
            return [y, x + seq]
        else:
            raise NotImplementedError

    def get_area(dig_plan: list[list[int, int]]) -> int:
        dig_map = [[0, 0]]
        cur_y, cur_x = dig_map[0]
        perimeter = 0
        for way, seq in dig_plan:
            perimeter += seq
            next_y, next_x = get_next_corner(cur_y, cur_x, way, seq)
            dig_map.append([next_y, next_x])
            cur_y, cur_x = next_y, next_x
        assert dig_map[0] == dig_map[-1] == [0, 0]

        area = 0 # compute area using triangle formula / shoelace formula
        for i in range(len(dig_map) - 1):
            y1, x1 = dig_map[i]
            y2, x2 = dig_map[i + 1]
            area += 0.5 * ((x1 * y2) - (x2 * y1))
        
        return int(area + perimeter//2 + 1)

    
    area1 = get_area(dig_plan1)
    print(f'Part 1: {area1}') # 66993 - part 1


    area2 = get_area(dig_plan2)
    print(f'Part 2: {area2}') # 177243763226648 - part 2