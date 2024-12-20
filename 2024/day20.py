if __name__ == '__main__':
    print('Advent of Code 2024 - Day 20: Race Condition')

    with open('day20.txt') as f:
        step_track = {}
        for y, line in enumerate(f.read().strip().splitlines()):
            for x, char in enumerate(line):
                if char not in '.SE':
                    continue
                if char == 'S':
                    start = (y, x)
                elif char == 'E':
                    end = (y, x)
                step_track[(y, x)] = None

    def get_4n(coord: tuple[int, int]) -> list[tuple[int, int]]:
        y, x = coord
        return [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]

    current = start
    step_track[current] = 0
    step = 1
    visited = {start}
    while current != end:
        for next_pos in get_4n(current):
            if next_pos in step_track and next_pos not in visited:
                current = next_pos
                break
        visited.add(current)
        step_track[current] = step
        step += 1


    # part 1

    def get_cheat1(coord: tuple[int, int]) -> list[tuple[int, int]]:
        y, x = coord
        ends = [(y, x+2), (y, x-2), (y+2, x), (y-2, x)]
        return [[pos, 2] for pos in ends if pos in step_track]

    total_cheats1 = 0
    for coord in step_track.keys():
        for end_cheat in get_cheat1(coord):
            cheat_pos, cheat_step = end_cheat
            if step_track[cheat_pos] - step_track[coord] - cheat_step >= 100:
                total_cheats1 += 1

    print(f'Part 1: {total_cheats1}') # 1393


    # part 2

    def get_cheat2(coord: tuple[int, int]) -> list[tuple[int, int]]:
        y, x = coord
        cheat_end = []
        for dy in range(-20, 21):
            for dx in range(-20, 21):
                cheat_step = abs(dy) + abs(dx)
                cheat_coord = (y + dy, x + dx)
                if cheat_step <= 20 and cheat_coord in step_track:
                    cheat_end.append([cheat_coord, cheat_step])

        return cheat_end

    total_cheats2 = 0
    for coord in step_track.keys():
        for end_cheat in get_cheat2(coord):
            cheat_pos, cheat_step = end_cheat
            if step_track[cheat_pos] - step_track[coord] - cheat_step >= 100:
                total_cheats2 += 1

    print(f'Part 2: {total_cheats2}') # 990096

