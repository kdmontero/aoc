def bfs(map_, start_node):
    visited = set()
    queue = {start_node}

    while queue:
        temp_queue = set()
        for pipe in queue:
            for connection in map_[pipe]:
                if connection not in visited:
                    temp_queue.add(connection)
            visited.add(pipe)
        queue = temp_queue
    return visited

def group_qty(map_):
    groups = 0
    overall_visited = set()

    for node in map_:
        if node not in overall_visited:
            overall_visited |= bfs(map_, node)
            groups += 1

    return groups

def main():
    print('Advent of Code 2017 - Day 12')

    with open('day12.txt') as f:
        pipes = {}
        for line in f.read().splitlines():
            key, values = line.split(' <-> ')
            connections = [int(v) for v in values.split(', ')]
            pipes[int(key)] = connections

    print(f'Part 1: {len(bfs(pipes, 0))}') # 141 - part 1

    print(f'Part 2: {group_qty(pipes)}') # 171 - part 2


if __name__ == '__main__':
    main()
