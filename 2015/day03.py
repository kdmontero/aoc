with open('day03.txt') as f:
    directions = list(f.readline())

class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def move(self, direction):
        if direction == '^':
            self.y += 1
        elif direction == 'v':
            self.y -= 1
        if direction == '<':
            self.x -= 1
        elif direction == '>':
            self.x += 1

# part 1
visited = {(0,0)}
santa = Santa()
for direction in directions:
    santa.move(direction)
    visited.add((santa.x, santa.y))

print(f'Part 1: {len(visited)}') # 2081


# part 2
real = Santa()
robo = Santa()
visited = set()
for i, direction in enumerate(directions):
    if i % 2 == 0:
        real.move(direction)
        visited.add((real.x, real.y))
    else:
        robo.move(direction)
        visited.add((robo.x, robo.y))

print(f'Part 2: {len(visited)}') # 2341