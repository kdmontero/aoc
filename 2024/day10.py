if __name__ == '__main__':
    print("Advent of Code 2024 - Day 10: Hoof It")

    with open('day10.txt') as f:
        grid = {}
        trailheads = set()
        for y, line in enumerate(f.read().strip().splitlines()):
            for x, num in enumerate(line):
                grid[(y, x)] = int(num)

                if num == '0':
                    trailheads.add((y, x))

    def get_4n(coords: tuple[int, int]) -> list[tuple[int, int]]:
        y, x = coords
        return [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]


    # part 1

    total_score = 0
    for trailhead in trailheads:
        cur_level = 1
        queue = set(get_4n(trailhead))
        while cur_level < 9:
            next_queue = set()
            for cur_pos in queue:
                if grid.get(cur_pos) != cur_level:
                    continue
                for n_coord in get_4n(cur_pos):
                    if grid.get(n_coord) == cur_level + 1:
                        next_queue.add(n_coord)
            queue = next_queue
            cur_level += 1
        total_score += len(queue)

    print(f'Part 1: {total_score}') # 822


    # part 2

    total_rating = 0
    for trailhead in trailheads:
        cur_level = 1
        queue = get_4n(trailhead)
        while cur_level < 9:
            next_queue = []
            for cur_pos in queue:
                if grid.get(cur_pos) != cur_level:
                    continue
                for n_coord in get_4n(cur_pos):
                    if grid.get(n_coord) == cur_level + 1:
                        next_queue.append(n_coord)
            queue = next_queue
            cur_level += 1
        total_rating += len(queue)

    print(f'Part 2: {total_rating}') # 1801

