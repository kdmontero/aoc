import re

if __name__ == '__main__':
    print('Advent of Code 2022 - Day 15')

    with open('day15.txt') as f:
        sensors = []
        for line in f.read().splitlines():
            given = re.findall('(-?\d+)', line)
            sensor_x, sensor_y = int(given[0]), int(given[1])
            beacon_x, beacon_y = int(given[2]), int(given[3])
            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            sensors.append([sensor_x, sensor_y, beacon_x, beacon_y, distance])


    # part 1

    no_beacon = set()
    for sensor in sensors:
        sensor_x, sensor_y, _, _, distance = sensor
        if distance < abs(sensor_y - 2_000_000):
            continue

        horizontal = (distance - abs(sensor_y - 2_000_000))
        for i in range(horizontal + 1):
            no_beacon.add((sensor_x + i, 2_000_000))
            no_beacon.add((sensor_x - i, 2_000_000))

    for sensor in sensors:
        _, _, beacon_x, beacon_y, distance = sensor
        no_beacon -= {(beacon_x, beacon_y)}

    print(f'Part 1: {len(no_beacon)}') # 5688618


    # part 2

    def remove_range(space: list[int], span: list[int]) -> None | list[int]:
        space_start, space_end = space # o - existing space
        span_start, span_end = span # x - to be deleted

        # ooooo..... space
        # ......xxxx span
        if space_end < span_start:
            return space

        # ....oooooo
        # xxxx......
        if span_end < space_start:
            return space

        # ...oooo...
        # ..xxxxxx..
        if span_start <= space_start <= space_end <= span_end:
            return None
        
        # ..oooooo..
        # ....xx....
        if space_start < span_start <= span_end < space_end:
            return [space_start, span_start-1, span_end+1, space_end]

        # ..ooooo...
        # .....xxxx.
        if space_start < span_start <= space_end <= span_end:
            return [space_start, span_start-1]

        # ....ooooo.
        # ..xxxx....
        if span_start < space_start <= span_end <= space_end:
            return [span_end+1, space_end]

    
    spaces = {i: [0, 4_000_000] for i in range(0,4_000_001)}
    for sensor in sensors:
        sensor_x, sensor_y, _, _, distance = sensor
        lower_bound = max(0, sensor_y - distance)
        upper_bound = min(4_000_000, sensor_y + distance)

        for y in range(lower_bound, upper_bound+1):
            horizontal = (distance - abs(sensor_y - y))
            new_space = []
            for i in range(0, len(spaces[y]), 2):
                space = remove_range(
                    [spaces[y][i], spaces[y][i+1]],
                    [sensor_x - horizontal, sensor_x + horizontal]
                )

                if space is not None:
                    new_space.extend(space)

            spaces[y] = new_space

    for y, space in spaces.items():
        if space != []:
            frequency = space[0] * 4_000_000 + y
            break

    print(f'Part 2: {frequency}') # 12625383204261
