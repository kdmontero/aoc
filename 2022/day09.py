from __future__ import annotations

class Knot:
    def __init__(self) -> None:
        self.x: int = 0
        self.y: int = 0
        self.tail: Knot = None

    def adjust_tail(self) -> None:
        if self.tail is None:
            return

        if all((
            abs(self.x - self.tail.x) <= 1, 
            abs(self.y - self.tail.y) <= 1,
        )):
            return

        if (self.x > self.tail.x) and (self.y > self.tail.y):
            self.tail.x += 1
            self.tail.y += 1
        elif (self.x > self.tail.x) and (self.y < self.tail.y):
            self.tail.x += 1
            self.tail.y -= 1
        elif (self.x < self.tail.x) and (self.y > self.tail.y):
            self.tail.x -= 1
            self.tail.y += 1
        elif (self.x < self.tail.x) and (self.y < self.tail.y):
            self.tail.x -= 1
            self.tail.y -= 1
        elif (self.x > self.tail.x) and (self.y == self.tail.y):
            self.tail.x += 1
        elif (self.x < self.tail.x) and (self.y == self.tail.y):
            self.tail.x -= 1
        elif (self.x == self.tail.x) and (self.y > self.tail.y):
            self.tail.y += 1
        elif (self.x == self.tail.x) and (self.y < self.tail.y):
            self.tail.y -= 1
        

    def move_head(self, direction: str) -> None:
        if direction == 'U':
            self.y -= 1
        elif direction == 'D':
            self.y += 1
        elif direction == 'L':
            self.x -= 1
        elif direction == 'R':
            self.x += 1


if __name__ == '__main__':
    print('Advent of Code 2022 - Day 09')

    with open('day09.txt') as f:
        motions = []
        for line in f.read().splitlines():
            direction, step = line.split()
            motions.append([direction, int(step)])


    # part 1 

    head1 = Knot()
    tail1 = Knot()
    head1.tail = tail1
    tail_visited1 = {(0,0)}

    for motion in motions:
        direction, step = motion
        for _ in range(step):
            head1.move_head(direction)
            head1.adjust_tail()
            tail_visited1.add((tail1.y, tail1.x))

    print(f'Part 1: {len(tail_visited1)}') # 6494

    
    # part 2

    string = {0: Knot()}
    for i in range(1, 10):
        string[i] = Knot()
        string[i-1].tail = string[i]

    tail2 = string[9]
    tail_visited2 = {(0,0)}

    for motion in motions:
        direction, step = motion
        for _ in range(step):
            head2 = string[0]
            head2.move_head(direction)

            while head2 is not tail2:
                head2.adjust_tail()
                head2 = head2.tail

            tail_visited2.add((head2.y, head2.x))


    print(f'Part 2: {len(tail_visited2)}') # 2691
