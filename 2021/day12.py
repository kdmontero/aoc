from collections import defaultdict

if __name__ == '__main__':
    print("Advent of Code 2021 - Day 12: Passage Pathing")

    with open('day12.txt') as f:
        connection = defaultdict(list)
        small_caves = set()
        for line in f.read().splitlines():
            node1, node2 = line.split('-')
            connection[node1].append(node2)
            connection[node2].append(node1)

    # part 1

    total_paths1 = 0
    def bt1(path):
        '''backtracking dfs'''
        global total_paths1
        last_cave = path[-1]
        for cave in connection[last_cave]:
            if cave.islower() and cave in path:
                continue
            elif cave == 'end':
                total_paths1 += 1
            else:
                bt1(path + [cave])
        return

    bt1(['start'])

    print(f'Part 1: {total_paths1}') # 4104


    # part 2

    total_paths2 = 0
    def bt2(path, has_seen_twice):
        '''backtracking dfs'''
        global total_paths2
        last_cave = path[-1]
        for cave in connection[last_cave]:
            if cave == 'end':
                total_paths2 += 1
            elif cave == 'start':
                continue
            elif cave.islower():
                if cave in path and has_seen_twice:
                    continue
                elif cave not in path and not has_seen_twice:
                    bt2(path + [cave], False)
                else:
                    bt2(path + [cave], True)
            else:
                bt2(path + [cave], has_seen_twice)
        return

    bt2(['start'], False)

    print(f'Part 2: {total_paths2}') # 119760
