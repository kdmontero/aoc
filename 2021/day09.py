if __name__ == '__main__':
    print('Advent of Code 2021 - Day 09')

    with open('day09.txt') as f:
        hmap = {}
        for y, line in enumerate(f.read().splitlines()):
            for x, height in enumerate(list(line)):
                hmap[(y, x)] = int(height)

        y_max, x_max = y, x


    # part 1

    def get_n(y, x):
        return [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]

    def check_location(coordinates):
        y, x = coordinates
        if hmap[coordinates] == 9:
            return False

        for neighbor in get_n(y, x):
            if neighbor not in hmap:
                continue
            if hmap[coordinates] >= hmap[neighbor]:
                return False
        return True

    low_points = []
    risk_levels = 0
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            if check_location((y, x)):
                risk_levels += 1 + hmap[(y, x)]
                low_points.append((y, x))
                
    print(f'Part 1: {risk_levels}') # 631


    # part 2

    visited = set()
    def basin_size(coordinates):
        queue = get_n(*coordinates)
        basin = {coordinates}
        visited.add(coordinates)

        while queue:
            node = queue.pop(0)

            if any([
                (node in visited), 
                (node not in hmap), 
                (hmap.get(node) == 9)
            ]):
                continue
            
            basin.add(node)
            visited.add(node)

            for n in get_n(*node):
                if any([
                    (n in visited), 
                    (n in queue),
                    (n not in hmap), 
                    (hmap.get(n) == 9)
                ]):
                    continue

                queue.append(n)

        return len(basin)

    basins = []
    for low_point in low_points:
        if low_point in visited:
            continue
        basins.append(basin_size(low_point))

    largest = sorted(basins, reverse=True)

    print(f'Part 2: {largest[0] * largest[1] * largest[2]}') # 821560
