import heapq
import copy

class Node:
    def __init__(self, y, x, value):
        self.y = y
        self.x = x
        self.value = value
        self.lowest_path = 999_999

    def __lt__(self, other):
        return self.lowest_path < other.lowest_path

if __name__ == '__main__':
    print("Advent of Code 2021 - Day 15: Chiton")

    with open('day15.txt') as f:
        given_density = {}
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(line):
                given_density[(y, x)] = Node(y, x, int(char))
        height, width = y + 1, x + 1


    # part 1

    def find_n(coordinates, density):
        y, x = coordinates
        n = []
        if (y-1, x) in density:
            n.append(density[(y-1, x)])
        if (y+1, x) in density:
            n.append(density[(y+1, x)])
        if (y, x+1) in density:
            n.append(density[(y, x+1)])
        if (y, x-1) in density:
            n.append(density[(y, x-1)])
        return n

    def update_n_distances(coordinates, density):
        node = density[(coordinates)]
        for n in find_n(coordinates, density):
            n.lowest_path = min(n.lowest_path, node.lowest_path + n.value)

        return find_n(coordinates, density)

    def find_lowest_path(density):
        y_max, x_max = 0, 0
        for y, x in density:
            x_max = max(x, x_max) 
            y_max = max(y, y_max)

        visited = set()
        density[(0, 0)].lowest_path = 0
        queue = [density[(0, 0)]]
        heapq.heapify(queue)
        while (y_max, x_max) not in visited:
            node = heapq.heappop(queue)
            visited.add((node.y, node.x))
            for n in update_n_distances((node.y, node.x), density):
                if (n.y, n.x) not in visited and n not in queue:
                    heapq.heappush(queue, n)
            heapq.heapify(queue)

        return density[(y_max, x_max)].lowest_path
        
    print(f'Part 1: {find_lowest_path(copy.deepcopy(given_density))}') # 619


    # part 2

    density2 = copy.deepcopy(given_density)
    for y in range(height * 5):
        for x in range(width * 5):
            if (y, x) in density2:
                continue

            if (y, x-width) in density2:
                tiled_value_before = density2[(y, x-width)].value
            else:
                tiled_value_before = density2[(y-height, x)].value
            
            if tiled_value_before == 9:
                density2[(y, x)] = Node(y, x, 1)
            else:
                density2[(y, x)] = Node(y, x, tiled_value_before + 1)

    print(f'Part 2: {find_lowest_path(density2)}') # 2922
