with open('day13.txt') as f:
    target, busses = f.read().split('\n')
    target = int(target)
    busses = [[i, int(bus)] for i, bus in enumerate(busses.split(",")) if bus != 'x']

print(busses)
wait = 1000
id = None
for bus in busses:
    time = bus[1]
    while time < target:
        time += bus[1]
    if time-target < wait:
        wait = time-target
        id = bus[1]

print(f'Part 1: {id*wait}') # 2095

