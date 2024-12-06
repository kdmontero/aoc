from copy import deepcopy


if __name__ == '__main__':
    print('Advent of Code 2024 - Day 06')

    with open('day06.txt') as f:
        map_ = {}
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(line):
                map_[(y, x)] = char
                if char not in '.#':
                    init_guard = [y, x, char]
        
        height, width = y + 1, x + 1

    class Guard:
        def __init__(self, y: int, x: int, dir: str) -> None:
            self.y = y
            self.x = x
            self.dir = dir
            self.reached_end = False

        def walk(self) -> None:
            if self.dir == '^':
                self.y -= 1
            elif self.dir == 'v':
                self.y += 1
            elif self.dir == '<':
                self.x -= 1
            elif self.dir == '>':
                self.x += 1

        def turn(self) -> None:
            if self.dir == '^':
                self.dir = '>'
            elif self.dir == '>':
                self.dir = 'v'
            elif self.dir == 'v':
                self.dir = '<'
            elif self.dir == '<':
                self.dir = '^'

        def can_walk(self, map_: dict[tuple[int, int], str]) -> bool:
            if self.dir == '^':
                next_step = map_.get((guard.y - 1, guard.x))
            elif self.dir == 'v':
                next_step = map_.get((guard.y + 1, guard.x))
            elif self.dir == '>':
                next_step = map_.get((guard.y, guard.x + 1))
            elif self.dir == '<':
                next_step = map_.get((guard.y, guard.x - 1))

            if next_step == None:
                self.reached_end = True

            return next_step != '#'

        def walk_to_end(self, map_: dict[tuple[int, int], str]) -> None:
            if self.dir == '^':
                for j in range(self.y - 1, -1, -1):
                    if map_.get((j, self.x)) == '#':
                        self.y = j + 1
                        return
            elif self.dir == 'v':
                for j in range(self.y + 1, height):
                    if map_.get((j, self.x)) == '#':
                        self.y = j - 1
                        return
            elif self.dir == '>':
                for i in range(self.x + 1, width):
                    if map_.get((self.y, i)) == '#':
                        self.x = i - 1
                        return
            elif self.dir == '<':
                for i in range(self.x - 1, -1, -1):
                    if map_.get((self.y, i)) == '#':
                        self.x = i + 1
                        return

            self.reached_end = True

    guard = Guard(*init_guard)


    # part 1

    positions = set()
    while not guard.reached_end:
        if guard.can_walk(map_):
            positions.add((guard.y, guard.x))
            guard.walk()
        else:
            guard.turn()

    print(f'Part 1: {len(positions)}') # 4977


    # part 2

    def is_loop(guard: Guard, map_: dict[tuple[int, int], str]) -> bool:

        visited = set()
        while not guard.reached_end:
            if (guard.y, guard.x, guard.dir) in visited:
                return True

            if guard.can_walk(map_):
                visited.add((guard.y, guard.x, guard.dir))
                guard.walk_to_end(map_)
            else:
                guard.turn()

        return False

    loop_obstruction = 0
    obstructions = positions - {(init_guard[0], init_guard[1])}
    for obstruction in obstructions:
        map_[obstruction] = '#'
        guard = Guard(*init_guard)
        if is_loop(guard, map_):
            loop_obstruction += 1
        map_[obstruction] = '.'

    print(f'Part 2: {loop_obstruction}') # 1729

