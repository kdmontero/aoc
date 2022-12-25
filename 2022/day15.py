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


    print(f'Part 2: {0}') #
