if __name__ == '__main__':
    print("Advent of Code 2018 - Day 06: Chronal Coordinates")

    with open('day06.txt') as f:
        top = left = 9999
        bottom = right = 0
        size_of = {}
        for line in f.read().splitlines():
            y, x = line.split(', ')
            top = min(top, int(y))
            left = min(left, int(x))
            bottom = max(bottom, int(y))
            right = max(right, int(x))
            size_of[int(y), int(x)] = 0


    def get_distance(point1, point2):
        y1, x1 = point1
        y2, x2 = point2
        return abs(x1 - x2) + abs(y1 - y2)

    infinite = set()
    safe_region = 0
    for y in range(top, bottom + 1):
        for x in range(left, right + 1):
            distance = 99999999
            has_equal = False
            safe_region_distance = 0

            for coord in size_of.keys():
                coord_distance = get_distance((y, x), coord)
                safe_region_distance += coord_distance
                if coord_distance < distance:
                    distance = coord_distance
                    closest = coord
                    has_equal = False
                elif coord_distance == distance:
                    has_equal = True

            if not has_equal:
                size_of[closest] += 1
                if (y in [top, bottom]) or (x in [left, right]):
                    infinite.add(closest)

            if safe_region_distance < 10000:
                safe_region += 1

    max_area = 0
    for coord in size_of.keys():
        if coord not in infinite:
            max_area = max(max_area, size_of[coord])

    print(f'Part 1: {max_area}') # 3909

    print(f'Part 2: {safe_region}') # 36238
