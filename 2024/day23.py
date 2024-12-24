from collections import defaultdict
if __name__ == '__main__':
    print('Advent of Code 2024 - Day 23: LAN Party')

    with open('day23.txt') as f:
        network = defaultdict(set)
        for line in f.read().strip().splitlines():
            node1, node2 = line.split('-')
            network[node1].add(node2)
            network[node2].add(node1)


    # part 1

    tri_network = []
    for node1 in network:
        if not(node1.startswith('t')):
            continue

        for node2 in network[node1]:
            for node3 in network[node2]:
                if node3 in network[node1]:
                    trio = {node1, node2, node3}
                    if trio not in tri_network:
                        tri_network.append(trio)

    print(f'Part 1: {len(tri_network)}') # 1327
    
    print(f'Part 2: {0}') #

