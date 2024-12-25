from __future__ import annotations
import copy


class Cart:
    instances = 0

    def __init__(self, dir: str, x: int, y: int) -> None:
        self.dir = dir
        self.x = x
        self.y = y
        self.count = 0
        self.id = Cart.instances
        Cart.instances += 1
        

    def __lt__(self, other: Cart) -> None:
        if self.y < other.y:
            return True
        elif self.y == other.y:
            if self.x < other.x:
                return True
        return False

    def __repr__(self):
        return f'Cart({self.dir}, {self.x}, {self.y})'

    def __hash__(self):
        return hash(self.id)

    def move(self) -> tuple[int, int]:
        if self.dir == '>':
            self.x, self.y = self.x+1, self.y
        elif self.dir == '<':
            self.x, self.y = self.x-1, self.y
        elif self.dir == '^':
            self.x, self.y = self.x, self.y-1
        elif self.dir == 'v':
            self.x, self.y = self.x, self.y+1
        return (self.x, self.y)

    def turn(self, front_rail) -> None:
        if any((
            self.dir in '<>' and front_rail == '-',
            self.dir in 'v^' and front_rail == '|'
        )):
            return

        elif front_rail == '\\':
            if self.dir == '>':
                self.dir = 'v'
            elif self.dir == '<':
                self.dir = '^'
            elif self.dir == 'v':
                self.dir = '>'
            elif self.dir == '^':
                self.dir = '<'

        elif front_rail == '/':
            if self.dir == '>':
                self.dir = '^'
            elif self.dir == '<':
                self.dir = 'v'
            elif self.dir == 'v':
                self.dir = '<'
            elif self.dir == '^':
                self.dir = '>'

        elif front_rail == '+':
            if self.count % 3 == 0:
                if self.dir == '^':
                    self.dir = '<'
                elif self.dir == 'v':
                    self.dir = '>'
                elif self.dir == '<':
                    self.dir = 'v'
                elif self.dir == '>':
                    self.dir = '^'
            elif self.count % 3 == 2:
                if self.dir == '^':
                    self.dir = '>'
                elif self.dir == 'v':
                    self.dir = '<'
                elif self.dir == '<':
                    self.dir = '^'
                elif self.dir == '>':
                    self.dir = 'v'
            self.count += 1
        return


if __name__ == '__main__':
    print("Advent of Code 2018 - Day 13: Mine Cart Madness")

    Track = dict[tuple[int, int], str | list[Cart]]
    with open('day13.txt') as f:
        carts = []
        track = {}
        rails_only = {}
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(line):
                if char in '<>^v':
                    cart = Cart(char, x, y)
                    track[(x, y)] = cart
                    carts.append(cart)

                    if char in 'v^':
                        rails_only[(x, y)] = '|'
                    elif char in '<>':
                        rails_only[(x, y)] = '-'

                elif char in r'-|\/+':
                    track[(x, y)] = char
                    rails_only[(x, y)] = char
    height = y
    width = x


    # part 1
    track1 = copy.deepcopy(track)
    carts1 = copy.deepcopy(carts)
    while True:
        new_carts = []
        for cart in carts1:
            prev_x, prev_y = cart.x, cart.y
            x, y = cart.move()
            next_pos = track1.get((x, y))
            if type(next_pos) == Cart:
                break

            cart.turn(next_pos)
            new_carts.append(cart)
            track1[(x, y)] = cart
            track1[(prev_x, prev_y)] = rails_only[(prev_x, prev_y)]
        else:
            carts1= sorted(new_carts)
            continue
        break

    print(f'Part 1: {x},{y}') # 80,100


    # part 2
    track2 = copy.deepcopy(track)
    carts2 = copy.deepcopy(carts)
    destroyed = set()
    while True:
        new_carts = set()
        for cart in carts2:
            if cart in destroyed:
                continue
            prev_x, prev_y = cart.x, cart.y
            x, y = cart.move()
            next_pos = track2.get((x, y))
            if type(next_pos) == Cart:
                destroyed.add(next_pos)
                destroyed.add(cart)
                track2[(prev_x, prev_y)] = rails_only[(prev_x, prev_y)]
                track2[(x, y)] = rails_only[(x, y)]
                continue
            cart.turn(next_pos)
            new_carts.add(cart)
            track2[(x, y)] = cart
            track2[(prev_x, prev_y)] = rails_only[(prev_x, prev_y)]

        carts2 = sorted(list(new_carts - destroyed))
        if len(carts2) == 1:
            break

    print(f'Part 2: {carts2[0].x},{carts2[0].y}') # 16,99
