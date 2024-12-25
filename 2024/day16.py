import heapq as hq


if __name__ == '__main__':
    print("Advent of Code 2024 - Day 16: Reindeer Maze")

    with open('day16.txt') as f:
        tracks = set()
        start_dir = '>'
        start_y = start_x = des_y = des_x = None
        for y, line in enumerate(f.read().strip().splitlines()):
            for x, char in enumerate(line):
                if char == '#':
                    continue
                elif char == 'S':
                    start_y = y
                    start_x = x
                elif char == 'E':
                    des_y = y
                    des_x = x

                tracks.add((y, x))
    

    def get_n(
        score: int,
        y: int,
        x: int,
        dir: str
    ) -> list[tuple[int, int, str, int]]:

        neighbors = []
        if dir == '^':
            if (y, x - 1) in tracks:
                neighbors.append((score + 1000, y, x, '<'))
            if (y - 1, x) in tracks:
                neighbors.append((score + 1, y - 1, x, dir))
            if (y, x + 1) in tracks:
                neighbors.append((score + 1000, y, x, '>'))
        elif dir == 'v':
            if (y, x + 1) in tracks:
                neighbors.append((score + 1000, y, x, '>'))
            if (y + 1, x) in tracks:
                neighbors.append((score + 1, y + 1, x, dir))
            if (y, x - 1) in tracks:
                neighbors.append((score + 1000, y, x, '<'))
        elif dir == '>':
            if (y - 1, x) in tracks:
                neighbors.append((score + 1000, y, x, '^'))
            if (y, x + 1) in tracks:
                neighbors.append((score + 1, y, x + 1, dir))
            if (y + 1, x) in tracks:
                neighbors.append((score + 1000, y, x, 'v'))
        elif dir == '<':
            if (y + 1, x) in tracks:
                neighbors.append((score + 1000, y, x, 'v'))
            if (y, x - 1) in tracks:
                neighbors.append((score + 1, y, x - 1, dir))
            if (y - 1, x) in tracks:
                neighbors.append((score + 1000, y, x, '^'))

        return neighbors

    min_score = 999999999999
    valid_tiles = set()
    checked_node_score = {}

    found_end = False
    cur_score = 0
    queue = [(cur_score, start_y, start_x, start_dir, set())]
    hq.heapify(queue)

    while not found_end or cur_score <= min_score:
        cur_score, cur_y, cur_x, cur_dir, visited = hq.heappop(queue)
        for nscore, ny, nx, ndir in get_n(cur_score, cur_y, cur_x, cur_dir):
            if (ny, nx, ndir) in checked_node_score:
                if nscore < checked_node_score[(ny, nx, ndir)]:
                    checked_node_score[(ny, nx, ndir)] = nscore
                else:
                    continue
            if (nscore, ny, nx, ndir) not in queue:
                hq.heappush(queue, (nscore, ny, nx, ndir, visited|{(ny, nx)}))

        checked_node_score[(cur_y, cur_x, cur_dir)] = cur_score

        if (cur_y, cur_x) == (des_y, des_x):
            found_end = True
            valid_tiles |= visited
            min_score = cur_score
            
    # 1 minute run time
    print(f'Part 1: {min_score}') # 115500

    print(f'Part 2: {len(valid_tiles)}') # 679

