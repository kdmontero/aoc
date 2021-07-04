print('Advent of Code 2017 - Day 13')

class Layer:
    def __init__(self, depth, range_):
        self.depth = depth
        self.range_ = range_
        self.period = (range_ - 1) * 2

    def scan(self, picosecond):
        position = picosecond % self.period
        if position < self.range_:
            return position + 1
        else:
            return self.period - position + 1

    def __str__(self):
        return str(self.depth)

    __repr__ = __str__


with open('day13.txt') as f:
    layers = {}
    for line in f.read().splitlines():
        d, r = line.split(': ')
        layers[int(d)] = Layer(int(d), int(r))

# part 1
severity = 0
for d, layer in layers.items():
    if layer.scan(d) == 1:
        severity += layer.depth * layer.range_

print(f'Part 1: {severity}') # 1476


# part 2
delay = 0
while True:
    for d, layer in layers.items():
        if layer.scan(delay + d) == 1:
            break
    else:
        break

    delay += 1

print(f'Part 2: {delay}') # 3937334
