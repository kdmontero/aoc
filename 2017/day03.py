from collections import Counter

print("Advent of Code 2017 - Day 03: Spiral Memory")
given = '325489'

class Port:
    def __init__(self):
        self.x = 1
        self.y = 0
        self.dir = 'U' # impending movement
    
    def move(self, grid):
        if self.dir == 'U':
            if (self.y, self.x-1) in grid:
                self.y -= 1
            else:
                self.dir = 'L'
                self.x -= 1
        elif self.dir == 'L':
            if (self.y+1, self.x) in grid:
                self.x -= 1
            else:
                self.dir = 'D'
                self.y += 1
        elif self.dir == 'D':
            if (self.y, self.x+1) in grid:
                self.y += 1
            else:
                self.dir = 'R'
                self.x += 1
        elif self.dir == 'R':
            if (self.y-1, self.x) in grid:
                self.x += 1
            else:
                self.dir = 'U'
                self.y -= 1

# part 1
access = int(given)
port1 = Port()
grid1 = {(0, 0): 1, (port1.y, port1.x): 2}
for i in range(3, access+1):
    port1.move(grid1)
    grid1[(port1.y, port1.x)] = i

print(f'Part 1: {abs(port1.x)+abs(port1.y)}') # 552
    

# part 2
def count_n(y, x, grid):
    n = 0
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            n += grid[(j, i)]
    return n

value = 1
grid2 = Counter({(0, 0): 1})
port2 = Port()

while value < access:
    value = count_n(port2.y, port2.x, grid2)
    grid2[(port2.y, port2.x)] = value
    port2.move(grid2)

print(f'Part 2: {value}') # 330785
