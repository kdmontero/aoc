import re

if __name__ == '__main__':
    print('Advent of Code 2022 - Day 16')

    with open('sample.txt') as f:
        tunnels = {}
        flow = {}

        for line in f.read().splitlines():
            flow_rate = int(re.findall('-?\d+', line)[0])
            valve, *tunnel = re.findall(r'\b[A-Z]{2}\b', line)
            tunnels[valve] = tunnel
            if (flow_rate != 0) or (valve == 'AA'):
                flow[valve] = flow_rate

    def get_min_dist(start: str, end: str) -> int:

        visited = set()
        queue = [start]
        step = 0
        while end not in visited:
            temp_queue = []
            step += 1
            for current in queue:
                for node in tunnels[current]:
                    if node in visited or node in queue:
                        continue
                    if node == end:
                        return step
                    temp_queue.append(node)
                else:
                    visited.add(current)
                    queue = temp_queue

    paths = {}
    for start in flow:
        paths[start] = {}
        for end in flow:
            if start == end:
                continue
            distance = get_min_dist(start, end)
            paths[start][end] = distance

    # part 1

    # implement A*
    '''
    max_pressure = 0
    visited = set()
    queue = [('AA', 0, 0)]
    while True:
        temp_queue = []
        for current in queue:
            node, time, pressure = current
            for n_node in paths[node]:
                if n_node in visited or n_node in queue:
                    pass
    '''

    print(f'Part 1: {0}') #


    print(f'Part 2: {0}') #
