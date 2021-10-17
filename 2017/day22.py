import copy

if __name__ == '__main__':
    print('Advent of Code 2017 - Day 22')

    with open('day22.txt') as f:
        given_infected_nodes = set()
        for y, line in enumerate(f.read().splitlines()):
            for x, node in enumerate(line):
                if node == '#':
                    given_infected_nodes.add((y,x))

    class Virus:
        
        def __init__(self, y, x, direction):
            self.y = y
            self.x = x
            self.direction = direction

        def turn_right(self):
            if self.direction == 'U':
                self.direction = 'R'
            elif self.direction == 'D':
                self.direction = 'L'
            elif self.direction == 'R':
                self.direction = 'D'
            elif self.direction == 'L':
                self.direction = 'U'
            
        def reverse(self):
            if self.direction == 'U':
                self.direction = 'D'
            elif self.direction == 'D':
                self.direction = 'U'
            elif self.direction == 'R':
                self.direction = 'L'
            elif self.direction == 'L':
                self.direction = 'R'
            
        def turn_left(self):
            if self.direction == 'U':
                self.direction = 'L'
            elif self.direction == 'D':
                self.direction = 'R'
            elif self.direction == 'R':
                self.direction = 'U'
            elif self.direction == 'L':
                self.direction = 'D'

        def forward(self):
            if self.direction == 'U':
                self.y -= 1
            elif self.direction == 'D':
                self.y += 1
            elif self.direction == 'R':
                self.x += 1
            elif self.direction == 'L':
                self.x -= 1

    # part 1

    virus = Virus(y//2, x//2, 'U')
    infected_nodes = copy.deepcopy(given_infected_nodes)
    bursts1 = 0
    
    for i in range(10_000):
        if (virus.y, virus.x) in infected_nodes:
            virus.turn_right()
            infected_nodes.remove((virus.y, virus.x))
        else:
            virus.turn_left()
            infected_nodes.add((virus.y, virus.x))
            bursts1 += 1
        
        virus.forward()

    print(f'Part 1: {bursts1}') # 5404
    
    
    # part 2

    virus = Virus(y//2, x//2, 'U')
    infected_nodes = copy.deepcopy(given_infected_nodes)
    weakened_nodes = set()
    flagged_nodes = set()
    bursts2 = 0

    for i in range(10_000_000):
        if (virus.y, virus.x) in infected_nodes:
            virus.turn_right()
            infected_nodes.remove((virus.y, virus.x))
            flagged_nodes.add((virus.y, virus.x))
        
        elif (virus.y, virus.x) in weakened_nodes:
            weakened_nodes.remove((virus.y, virus.x))
            infected_nodes.add((virus.y, virus.x))
            bursts2 += 1

        elif (virus.y, virus.x) in flagged_nodes:
            virus.reverse()
            flagged_nodes.remove((virus.y, virus.x))

        else:
            virus.turn_left()
            weakened_nodes.add((virus.y, virus.x))
        
        virus.forward()

    print(f'Part 2: {bursts2}') # 2511672
