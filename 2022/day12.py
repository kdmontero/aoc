import copy

if __name__ == '__main__':
    print('Advent of Code 2022 - Day 12')

    with open('day12.txt') as f:
        map_ = {}
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(line):
                value = ord(char)
                if char == 'S':
                    orig_start = (y, x)
                    value = ord('a')
                if char == 'E':
                    orig_end = (y, x)
                    value = ord('z')
                map_[(y, x)] = value

    def shortest_path(start: tuple, connections: dict, end: set) -> int:
        visited = set()
        queue = {start}
        steps = 0
        while True:
            temp_queue = set()
            while queue:
                current_node = queue.pop()
                visited.add(current_node)
                for neighbor in connections[current_node]:
                    if neighbor not in (visited | queue):
                        temp_queue.add(neighbor)
            if (end & visited):
                break
            queue = temp_queue
            steps += 1

        return steps


    # part 1

    start1 = orig_start
    end1 = {orig_end}

    connections1 = {}
    for y, x in map_.keys():
        paths = []
        for neighbor in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
            if map_.get((neighbor)) is None:
                continue
            if map_.get((neighbor)) - map_.get((y, x)) <= 1:
                paths.append(neighbor)
        connections1[(y, x)] = paths


    print(f'Part 1: {shortest_path(start1, connections1, end1)}') # 420


    # part 2

    start2 = orig_end
    end2 = set()
    for coordinate, value in map_.items():
        if value == ord('a'):
            end2.add(coordinate)

    connections2 = {}
    for y, x in map_.keys():
        paths = []
        for neighbor in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
            if map_.get((neighbor)) is None:
                continue
            if map_.get((neighbor)) - map_.get((y, x)) >= -1:
                paths.append(neighbor)
        connections2[(y, x)] = paths


    print(f'Part 2: {shortest_path(start2, connections2, end2)}') # 414
