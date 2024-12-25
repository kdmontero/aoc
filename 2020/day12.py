from collections import deque
import math

print("Advent of Code 2020 - Day 12: Rain Risk")
with open('day12.txt') as f:
    nav = [(line[0], int(line[1:])) for line in f.read().split('\n')]

class Ship():
    def __init__(self):
        self.facing = 'E'
        self.x = 0
        self.y = 0
        self.rotation = deque(['E', 'S', 'W', 'N'])
        self.way_x = 10
        self.way_y = 1

    def north(self, value):
        self.y += value
    
    def south(self, value):
        self.y -= value
    
    def east(self, value):
        self.x += value
    
    def west(self, value):
        self.x -= value

    def left(self, value):
        shift = value//90
        self.rotation.rotate(shift)
        self.facing = self.rotation[0]
    
    def right(self, value):
        shift = -value//90
        self.rotation.rotate(shift)
        self.facing = self.rotation[0]
    
    def forward(self, value):
        if self.facing == 'N':
            self.north(value)
        elif self.facing == 'E':
            self.east(value)
        elif self.facing == 'S':
            self.south(value)
        elif self.facing == 'W':
            self.west(value)
    
    def distance(self):
        return abs(self.x) + abs(self.y)
    
    def way_forward(self, value):
        self.x += value * self.way_x
        self.y += value * self.way_y

    def way_north(self, value):
        self.way_y += value
    
    def way_south(self, value):
        self.way_y -= value
    
    def way_east(self, value):
        self.way_x += value
    
    def way_west(self, value):
        self.way_x -= value

    def way_ccw(self, value):
        theta = math.atan2(self.way_y, self.way_x) + math.radians(value)
        r = math.sqrt(self.way_x**2 + self.way_y**2)
        self.way_x = round(r * math.cos(theta))
        self.way_y = round(r * math.sin(theta))

    def way_cw(self, value):
        theta = math.atan2(self.way_y, self.way_x) - math.radians(value)
        r = math.sqrt(self.way_x**2 + self.way_y**2)
        self.way_x = round(r * math.cos(theta))
        self.way_y = round(r * math.sin(theta))

# part 1
ship1 = Ship()
for action, value in nav:
    if action == 'N':
        ship1.north(value)
    elif action == 'E':
        ship1.east(value)
    elif action == 'S':
        ship1.south(value)
    elif action == 'W':
        ship1.west(value)
    elif action == 'L':
        ship1.left(value)
    elif action == 'R':
        ship1.right(value)
    elif action == 'F':
        ship1.forward(value)

print(f'Part 1: {ship1.distance()}') # 362


# part 2
ship2 = Ship()
for action, value in nav:
    if action == 'N':
        ship2.way_north(value)
    elif action == 'E':
        ship2.way_east(value)
    elif action == 'S':
        ship2.way_south(value)
    elif action == 'W':
        ship2.way_west(value)
    elif action == 'L':
        ship2.way_ccw(value)
    elif action == 'R':
        ship2.way_cw(value)
    elif action == 'F':
        ship2.way_forward(value)

print(f'Part 2: {ship2.distance()}') # 29895
