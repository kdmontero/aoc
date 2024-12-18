if __name__ == '__main__':
    print('Advent of Code 2024 - Day 12')

    #with open('day0.txt') as f:
    with open('day12.txt') as f:
        grid = {}
        for y, line in enumerate(f.read().strip().splitlines()):
            for x, char in enumerate(line):
                grid[(y, x)] = char

        height, width = y, x


    # part 1

    def get_4n(coords: tuple[int, int]) -> list[tuple[int, int]]:
        y, x = coords
        return [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

    def get_price(plot: set[tuple[int, int]]) -> int:
        perimeter = 0
        for plant in plot:
            for neighbor in get_4n(plant):
                if neighbor not in plot:
                    perimeter += 1
        return len(plot) * perimeter

    queue = set(grid)
    visited = set()
    regions = []
    while queue:
        plant = queue.pop()
        plant_queue = {plant}
        plant_char = grid.get(plant)
        plot = set()
        while plant_queue:
            current = plant_queue.pop()
            for n in get_4n(current):
                if grid.get(n) == plant_char and n not in visited:
                    plant_queue.add(n)
            visited.add(current)
            plot.add(current)
            queue -= {current}

        regions.append(plot)

    total_price = 0
    for region in regions:
        total_price += get_price(region)

    print(f'Part 1: {total_price}') # 1461806


    print(f'Part 2: {0}') #

