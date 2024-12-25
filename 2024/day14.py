from __future__ import annotations

import os
import time
from collections import defaultdict


class Robot:
    height = 103
    width = 101
    robots = []
    positions = defaultdict(int)
    seconds = 0

    def __init__(self, px: int, py: int, vx: int, vy: int) -> None:
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        Robot.robots.append(self)
        Robot.positions[(self.px, self.py)] += 1

    def move_after(self, steps: int) -> None:
        Robot.positions[(self.px, self.py)] -= 1
        self.px = (self.px + (self.vx * steps)) % self.width
        self.py = (self.py + (self.vy * steps)) % self.height
        self.positions[(self.px, self.py)] += 1
    
    @classmethod
    def all_move_after(cls, steps: int) -> None:
        for robot in cls.robots:
            robot.move_after(steps)
        cls.seconds += steps


if __name__ == '__main__':
    print("Advent of Code 2024 - Day 14: Restroom Redoubt")

    with open('day14.txt') as f:
        for line in f.read().strip().splitlines():
            pos, vel = line.strip().replace('=', '').split()
            px, py = pos.replace('p', '').split(',')
            vx, vy = vel.replace('v', '').split(',')
            Robot(int(px), int(py), int(vx), int(vy))


    # part 1
    
    Robot.all_move_after(100)

    q1 = q2 = q3 = q4 = 0
    height = Robot.height
    width = Robot.width
    for j in range(height):
        for i in range(width):
            if 0 <= j < height//2 and width//2 < i < width:
                q1 += Robot.positions[(i, j)]
            elif 0 <= j < height//2 and 0 <= i < width//2:
                q2 += Robot.positions[(i, j)]
            elif height//2 < j < height and 0 <= i < width//2:
                q3 += Robot.positions[(i, j)]
            elif height//2 < j < height and width//2 < i < width:
                q4 += Robot.positions[(i, j)]

    safety_factor = q1 * q2 * q3 * q4

    print(f'Part 1: {safety_factor}') # 236628054


    # part 2

    def find_easter_egg(animate: bool = False, show_end: bool = False):
        found = False
        while not found:
            Robot.all_move_after(1)
            grid = []
            for j in range(height):
                line = ''
                for i in range(width):
                    if Robot.positions[(i, j)] > 0:
                        line += '#'
                    else:
                        line += ' '
                grid.append(line)
                if '#########' in line:
                    found = True

            if animate:
                os.system('clear')
                print(Robot.seconds)
                print(*grid, sep='\n')
                # time.sleep(0.1) # animation delay

        if (not animate) and show_end:
            print(*grid, sep='\n')

        return Robot.seconds
        
    total_time = find_easter_egg(animate=False, show_end=False)

    print(f'Part 2: {total_time}') # 7584

