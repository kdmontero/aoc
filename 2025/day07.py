from collections import defaultdict


if __name__ == '__main__':
    print("Advent of Code 2025 - Day 07: Laboratories")

    with open('day07.txt') as f:
        splitter: set[tuple[int, int]] = set()
        start: tuple[int, int] = None

        for y, line in enumerate(f.read().strip().splitlines()):
            for x, char in enumerate(line):
                if char == '^':
                    splitter.add((y, x))
                elif char == 'S':
                    start = (y, x)
        height = y

    split_count = 0
    x_beam_count: dict[int, int] = defaultdict(int)
    x_beam_count[start[1]] = 1
    x_beam_set: set[int] = {start[1]}

    for y in range(start[0], height + 1):
        next_x_beam: set[int] = set()
        for x in x_beam_set:
            if (y, x) in splitter:
                split_count += 1
                next_x_beam |= {x+1, x-1}
                x_beam_count[x+1] += x_beam_count[x]
                x_beam_count[x-1] += x_beam_count[x]
                x_beam_count.pop(x, None)
            else:
                next_x_beam |= {x}
        x_beam_set = next_x_beam

    timelines = sum(x_beam_count.values())


    print(f'Part 1: {split_count}') # 1579

    print(f'Part 2: {timelines}') # 13418215871354

