from __future__ import annotations
import heapq


if __name__ == '__main__':
    print('Advent of Code 2023 - Day 17')

    with open('day17.txt') as f:
        grid = {}
        for y, line in enumerate(f.read().splitlines()):
            for x, num in enumerate(line):
                grid[(y, x)] = int(num)
        height, width = y, x
    
    class TileState:
        def __init__(
            self, 
            y: int, 
            x: int, 
            step: int, 
            way: str, 
            seq: int, 
        ) -> None:
            self.y = y
            self.x = x
            self.step = step
            self.way = way # 'U', 'D', 'L', 'R'
            self.seq = seq
    
        def __lt__(self, other: TileState) -> bool:
            global height
            global width
            self_score = abs(self.y - height) + abs(self.x - width)
            other_score = abs(other.y - height) + abs(other.x - width)
            if self.step + self_score < other.step + other_score:
                return True
            return False

    def get_n8(y: int, x: int) -> list[tuple[int, int]]:
        '''returns the coordinates of the neighbors in grid with 1, 4 dist.'''
        neighbors = []
        for ny, nx in [
            (y-1, x), (y+1, x), (y, x-1), (y, x+1),
            (y-4, x), (y+4, x), (y, x-4), (y, x+4)
        ]:
            if (ny, nx) in grid:
                neighbors.append((ny, nx))
        return neighbors

    def get_heat_of_n(y: int, x: int, ny: int, nx: int) -> int:
        '''Sums the heat going from (y, x) to (ny, nx)'''
        heat = 0
        if y == ny:
            if x > nx:
                for dx in range(x-1, nx-1, -1):
                    heat += grid[(y, dx)]
            elif x < nx:
                for dx in range(x+1, nx+1):
                    heat += grid[(y, dx)]
        elif x == nx:
            if y > ny:
                for dy in range(y-1, ny-1, -1):
                    heat += grid[(dy, x)]
            elif y < ny:
                for dy in range(y+1, ny+1):
                    heat += grid[(dy, x)]
        return heat

    distance = {} # dict of dict: distance[A][B] = distance of A-B. A, B are coords
    for y in range(height + 1):
        for x in range(width + 1):
            distance[(y, x)] = {}
            for ny, nx in get_n8(y, x):
                distance[(y, x)][(ny, nx)] = get_heat_of_n(y, x, ny, nx)


    # part 1
    def valid_n1(y: int, x: int, way: str, seq: int) -> list[tuple[int, int]]:
        '''returns the coordinates of valid neighbors'''
        if way == 'U':
            if seq < 3:
                neighbors = [(y-1, x), (y, x+1), (y, x-1)]
            else:
                neighbors = [(y, x+1), (y, x-1)]
        elif way == 'D':
            if seq < 3:
                neighbors = [(y+1, x), (y, x+1), (y, x-1)]
            else:
                neighbors = [(y, x+1), (y, x-1)]
        elif way == 'L':
            if seq < 3:
                neighbors = [(y, x-1), (y-1, x), (y+1, x)]
            else:
                neighbors = [(y-1, x), (y+1, x)]
        elif way == 'R':
            if seq < 3:
                neighbors = [(y, x+1), (y-1, x), (y+1, x)]
            else:
                neighbors = [(y-1, x), (y+1, x)]
        return [n for n in neighbors if grid.get(n) is not None]
    
    def find_min_heat_loss(
        queue: list[TileState], 
        min_step: int, 
        valid_n: Callable[[int, int, str, int], list[tuple[int, int]]]
    ) -> int:

        visited = set()
        while queue:
            cur_tile = heapq.heappop(queue)
            if (cur_tile.y, cur_tile.x) == (height, width):
                return cur_tile.step

            visited.add((cur_tile.y, cur_tile.x, cur_tile.way, cur_tile.seq))
            adj_n = valid_n(cur_tile.y, cur_tile.x, cur_tile.way, cur_tile.seq)
            for ny, nx in adj_n:
                if ny < cur_tile.y:
                    nway = 'U'
                elif ny > cur_tile.y:
                    nway = 'D'
                elif nx < cur_tile.x:
                    nway = 'L'
                elif nx > cur_tile.x:
                    nway = 'R'
                
                if nway == cur_tile.way:
                    nseq = cur_tile.seq + 1
                else:
                    nseq = min_step

                if (ny, nx, nway, nseq) in visited:
                    continue

                nstep = cur_tile.step + \
                    distance[(cur_tile.y, cur_tile.x)][(ny, nx)]
                heapq.heappush(queue, TileState(ny, nx, nstep, nway, nseq))
        return -1

    queue1 = [TileState(0, 0, 0, 'D', 3), TileState(0, 0, 0, 'R', 3)]
    min_heat_loss1 = find_min_heat_loss(queue1, 1, valid_n1)

    print(f'Part 1: {min_heat_loss1}') # 845


    # part 2
    def valid_n2(y: int, x: int, way: str, seq: int) -> list[tuple[int, int]]:
        '''returns the coordinates of valid neighbors with minimum of 4'''
        if way == 'U':
            if seq < 10:
                neighbors = [(y-1, x), (y, x+4), (y, x-4)]
            else:
                neighbors = [(y, x+4), (y, x-4)]
        elif way == 'D':
            if seq < 10:
                neighbors = [(y+1, x), (y, x+4), (y, x-4)]
            else:
                neighbors = [(y, x+4), (y, x-4)]
        elif way == 'L':
            if seq < 10:
                neighbors = [(y, x-1), (y-4, x), (y+4, x)]
            else:
                neighbors = [(y-4, x), (y+4, x)]
        elif way == 'R':
            if seq < 10:
                neighbors = [(y, x+1), (y-4, x), (y+4, x)]
            else:
                neighbors = [(y-4, x), (y+4, x)]
        return [n for n in neighbors if grid.get(n) is not None]

    queue2 = [TileState(0, 0, 0, 'D', 10), TileState(0, 0, 0, 'R', 10)]
    min_heat_loss2 = find_min_heat_loss(queue2, 4, valid_n2)

    print(f'Part 2: {min_heat_loss2}') # 993
