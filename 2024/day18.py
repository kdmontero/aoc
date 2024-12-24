if __name__ == '__main__':
    print('Advent of Code 2024 - Day 18: RAM Run')

    with open('day18.txt') as f:
        first_bytes = set()
        last_bytes = []
        for i, line in enumerate(f.read().strip().splitlines(), 1):
            x, y = line.split(',')
            if i <= 1024:
                first_bytes.add((int(x), int(y)))
            else:
                last_bytes.append((int(x), int(y)))


    # part 1

    def find_shortest_path(positions: set[tuple[int, int]]) -> int | None:
        cur_x, cur_y = 0, 0
        des_x, des_y = 70, 70
        steps = 0
        queue = {(0, 0)}
        visited = set()
        while queue:
            next_queue = set()
            for cur_x, cur_y in queue:
                if (cur_x, cur_y) == (des_x, des_y):
                    return steps

                # find valid neighbors
                neighbors = []
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    nx = cur_x + dx
                    ny = cur_y + dy
                    if nx < 0 or nx > 70 or ny < 0 or ny > 70:
                        continue
                    if (nx, ny) not in first_bytes:
                        neighbors.append((nx, ny))

                for nx, ny in neighbors:
                    if (nx, ny) in visited or (nx, ny) in next_queue or (nx, ny) in queue:
                        continue
                    next_queue.add((nx, ny))
                visited.add((cur_x, cur_y))
            queue = next_queue
            steps += 1
        else:
            return None

    print(f'Part 1: {find_shortest_path(first_bytes)}') # 334


    # part 2

    for byte in last_bytes:
        first_bytes |= {byte}
        if find_shortest_path(first_bytes) == None:
            break

    blocker_x, blocker_y = byte
    blocker = f'{blocker_x},{blocker_y}'

    print(f'Part 2: {blocker}') # 20,12

