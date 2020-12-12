import os
import time
from itertools import cycle
from collections import deque

class Asteroid:
    def __init__(self, ysym, xsym, slope, y0, x0, distance):
        self.ysym = ysym # symbol of y pos of asteroid relative to SS (space station)
        self.xsym = xsym # symbol of x pos of asteroid relative to SS
        self.slope = slope # slope of asteroid relative to SS
        self.y0 = y0 # y coordinate of asteroid
        self.x0 = x0 # x coordinate of asteroid
        self.distance = distance # distance of asteroid from SS

        # refers to 8 sections ranked in order of clockwise direction
        if ysym == -1 and xsym == 0: # positive y-axis
            self.section = 0
        elif ysym == -1 and xsym == 1: # quadrant 1
            self.section = 1
        elif ysym == 0 and xsym == 1: # positive x-axis
            self.section = 2
        elif ysym == 1 and xsym == 1: # quadrant 4
            self.section = 3
        elif ysym == 1 and xsym == 0: # negative y-axis
            self.section = 4
        elif ysym == 1 and xsym == -1: # quadrant 3
            self.section = 5
        elif ysym == 0 and xsym == -1: # negative x-axis
            self.section = 6
        elif ysym == -1 and xsym == -1: # quadrant 2
            self.section = 7

as_char = 'x' # asteroid
sp_char = ' ' # empty space
ss_char = '@' # SS

with open('day10.txt') as f:
    space = f.read().replace(".",sp_char).replace("#",as_char).split('\n')

asteroids = [] # list of ALL asteroids relative to SS
max_visible = 0
for y_ss in range(len(space)):
    for x_ss in range(len(space[0])):
        if space[y_ss][x_ss] == as_char:
            temp_asteroids = []
            sighted = []
            for y0 in range(len(space)):
                for x0 in range(len(space[0])):
                    if (space[y0][x0] == as_char) and not ((y0 == y_ss) and (x0 == x_ss)):
                        ydis = y0 - y_ss 
                        xdis = x0 - x_ss
                        ysym = -1 if (ydis < 0) else 1 if (ydis > 0) else 0
                        xsym = -1 if (xdis < 0) else 1 if (xdis > 0) else 0
                        slope = 0 if (ydis == 0) else "INF" if (xdis == 0) else ydis/xdis
                        distance = abs(ydis) + abs(xdis)
                        if [ysym, xsym, slope] not in sighted:
                            sighted.append([ysym, xsym, slope])
                        asteroid = Asteroid(ysym, xsym, slope, y0, x0, distance)
                        temp_asteroids.append(asteroid)
            if len(sighted) > max_visible:
                max_visible = len(sighted)
                asteroids = temp_asteroids
                ss_position = (x_ss, y_ss)

x_ss, y_ss = ss_position
space[y_ss] = space[y_ss][:x_ss]+ss_char+space[y_ss][x_ss+1:]
print(f'Part 1: {max_visible} at Space Station {ss_position}') # 214


# part 2
asteroids = sorted(asteroids, key=lambda x: (x.section, x.slope, x.distance))
line_of_sight = []
cur_slope = "INF"
temp = deque()
for asteroid in asteroids:
    if asteroid.slope == cur_slope:
        temp.append(asteroid)
    else:
        cur_slope = asteroid.slope
        line_of_sight.append(temp)
        temp = deque()
        temp.append(asteroid)
line_of_sight.append(temp)

target = 200
count = 0
in_order = []
for visible in cycle(line_of_sight):
    if visible:
        vaporized = visible.popleft()
        count += 1
        in_order.append(vaporized)
        if count == target:
            coordinates = (vaporized.x0, vaporized.y0)
            break

print(f'Part 2: {coordinates[0]*100 + coordinates[1]}') # 502

# visualized part 2
def blast(space, asteroid):
    x, y = asteroid.x0, asteroid.y0
    space[y] = space[y][:x]+sp_char+space[y][x+1:]

def start_giant_laser(space, target, asteroid_list):
    for asteroid in asteroid_list:
        if asteroid_list.index(asteroid) == target:
            break
        os.system("clear")
        blast(space, asteroid)
        print(*space, sep="\n")
        time.sleep(0.05)

# comment out below code to skip terminal animation
start_giant_laser(space, target, in_order)
print(f'Part 1: {max_visible} at Space Station {ss_position}') # 214
print(f'Part 2: {coordinates[0]*100 + coordinates[1]}') # 502