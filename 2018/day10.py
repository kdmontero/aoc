import re


if __name__ == '__main__':
    print("Advent of Code 2018 - Day 10: The Stars Align")

    with open('day10.txt') as f:
        pattern = re.compile(r'-?\d+')
        current_state = {}
        velocities = {}
        current_min_y = 999999
        current_max_y = 0
        for i, line in enumerate(f.read().splitlines()):
            point = [int(num) for num in pattern.findall(line)]
            current_state[i] = [point[0], point[1]]
            velocities[i] = [point[2], point[3]]
            current_min_y = min(current_min_y, point[1])
            current_max_y = max(current_max_y, point[1])


    seconds = 0
    while True:
        next_state = {}
        next_min_y = 999999
        next_max_y = 0
        for i, [x, y] in current_state.items():
            x_vel, y_vel = velocities[i]
            next_state[i] = [x + x_vel, y + y_vel]
            next_min_y = min(next_min_y, y + y_vel)
            next_max_y = max(next_max_y, y + y_vel)

        current_height = current_max_y - current_min_y
        next_height = next_max_y - next_min_y
        if next_height > current_height:
            break
        current_state = next_state
        current_min_y, current_max_y = next_min_y, next_max_y
        seconds += 1


    def print_message(state: dict) -> None:
        min_x = min(state.values(), key=lambda a: a[0])[0]
        max_x = max(state.values(), key=lambda a: a[0])[0]
        min_y = min(state.values(), key=lambda a: a[1])[1]
        max_y = max(state.values(), key=lambda a: a[1])[1]
        
        message = []
        for y in range(min_y, max_y + 1):
            line = ''
            for x in range(min_x, max_x + 1):
                if [x, y] in state.values():
                    line += '#'
                else:
                    line += ' '
            message.append(line)
        print(*message, sep='\n')

    print(f'Part 1: ') # AHFGRKEE
    print_message(current_state)

    print(f'Part 2: {seconds}') # 10243
