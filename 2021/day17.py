import re


if __name__ == '__main__':
    print('Advent of Code 2021 - Day 17')

    with open('day17.txt') as f:
        pattern = re.compile(r'(-?\d+)')
        matches = pattern.findall(f.read())
        x_start = int(matches[0])
        x_end = int(matches[1])
        y_end = int(matches[2])
        y_start = int(matches[3])


    # part 1 - shortcut formula given that y values are always negative

    highest_point = abs(y_end) * (abs(y_end)-1) //  2
    print(f'Part 1: {highest_point}') # 4278


    # part 2

    def will_reach_target(x_vel: int, y_vel: int) -> bool:
        x_pos, y_pos = 0, 0
        global x_start, x_end, y_start, y_end
        while x_pos <= x_end and y_pos >= y_end:
            x_pos += x_vel
            y_pos += y_vel
            x_vel = max(0, x_vel - 1)
            y_vel -= 1
            if x_start <= x_pos <= x_end and y_start >= y_pos >= y_end:
                return True
        return False


    count = 0

    for y_vel in range(y_end, -y_end):
        for x_vel in range(x_end + 1):
            if will_reach_target(x_vel, y_vel):
                count += 1

    print(f'Part 2: {count}') # 1994
