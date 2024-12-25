print("Advent of Code 2020 - Day 13: Shuttle Search")
with open('day13.txt') as f:
    target, buses = f.read().split('\n')
    target = int(target)
    buses = [
        [i, int(bus)] for i, bus in enumerate(buses.split(",")) if bus != 'x'
    ]

wait = 1000
id = None
for bus in buses:
    time = bus[1]
    while time < target:
        time += bus[1]
    if time-target < wait:
        wait = time-target
        id = bus[1]

print(f'Part 1: {id*wait}') # 2095


# part 2
timestamp = 0
offset1, bus1 = buses[0]
for offset2, bus2 in buses[1:]:
    init_step, step = 0, bus1
    if (timestamp + offset2) % bus2 == 0:
        found_immediately = True
    else:
        found_immediately = False

    while True:
        if found_immediately:
            break

        timestamp += step
        
        if (timestamp - offset1) % bus1 == (timestamp + offset2) % bus2 == 0:
            if not init_step: # find the timestamp where they will first meet
                init_step = timestamp
                resume = timestamp
            else: 
                # find the next timestamp where they will meet to know the 
                # cycle length or step
                step = timestamp - init_step
                
                # resume to the timestamp where the 2 buses first met
                timestamp = resume 
                break
    
    offset1, bus1 = init_step, step

print(f'Part 2: {timestamp}') # 598411311431841
