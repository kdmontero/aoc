from __future__ import annotations
import heapq

class TileState:
    def __init__(self, y: int, x: int, step: int, way: str, seq: int) -> None:
        self.y = y
        self.x = x
        self.step = step
        self.way = way # 'U', 'D', 'L', 'R'
        self.seq = seq
    
    def __lt__(self, other: TileState) -> bool:
        if self.step < other.step:
            return True
        return False
    
if __name__ == '__main__':
    print('Advent of Code 2023 - Day 17')

    with open('2.txt') as f:
        grid = {}
        for y, line in enumerate(f.read().splitlines()):
            for x, num in enumerate(line):
                grid[(y, x)] = int(num)
        height, width = y, x
    
    def get_n1(y: int, x: int) -> list[tuple[int, int]]:
        neighbors = []
        for ny, nx in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
            if (ny, nx) in grid:
                neighbors.append((ny, nx))
        return neighbors

    paths1 = {} # dict of dict: paths1[start][end] = distance from A to B
    for y in range(height + 1):
        for x in range(width + 1):
            paths1[(y, x)] = {}
            for ny, nx in get_n1(y, x):
                paths1[(y, x)][(ny, nx)] = grid[(ny, nx)]
    
    visited = set() # (A, B) where A is visited from B
    # shortest = {(0, 0): None} # stores the the source vertex for shortest path
    heap = [TileState(0, 0, 0, '', 0)] # stores the shortest path
    while heap:
        cur_tile = heapq.heappop(heap)
        if (cur_tile.y, cur_tile.x) == (height, width):
            print(cur_tile.step)
            break

        visited.add((cur_tile.y, cur_tile.x, cur_tile.way, cur_tile.seq))
        print(cur_tile.y, cur_tile.x, cur_tile.step, cur_tile.way, cur_tile.seq)
        for ny, nx in paths1[(cur_tile.y, cur_tile.x)]:

            if all((ny < cur_tile.y, cur_tile.way == 'U', cur_tile.seq == 3)):
                print(12341234)
                continue
            if all((ny > cur_tile.y, cur_tile.way == 'D', cur_tile.seq == 3)):
                print(12341234)
                continue
            if all((nx < cur_tile.x, cur_tile.way == 'L', cur_tile.seq == 3)):
                print(12341234)
                continue
            if all((nx > cur_tile.x, cur_tile.way == 'R', cur_tile.seq == 3)):
                print(12341234)
                continue

            if (ny, nx) == (height, width):
                print('--------')
                print(ny, nx, nway, nseq)
                print(cur_tile.y, cur_tile.x, cur_tile.step, cur_tile.way, cur_tile.seq)
                print('--------')
                print('-------------------')
                print(cur_tile.step + paths1[cur_tile.y, cur_tile.x][ny, nx])
                breakpoint()
                break

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
                nseq = 1

            if (ny, nx, nway, nseq) in visited:
                continue

            nstep = cur_tile.step + paths1[cur_tile.y, cur_tile.x][ny, nx]
            print('--------')
            print(ny, nx, nstep, nway, nseq)
            print(cur_tile.y, cur_tile.x, cur_tile.step, cur_tile.way, cur_tile.seq)
            print('--------')
            heapq.heappush(heap, TileState(ny, nx, nstep, nway, nseq))
        
        else:
            if len(visited) % 1000 == 0:
                print(len(heap), len(visited))
            continue
        break



    print(f'Part 1: {cur_tile.step}') # 854 too high


    print(f'Part 2: {0}') #