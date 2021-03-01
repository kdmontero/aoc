print('Advent of Code 2016 - Day 20')
with open('day20.txt') as f:
    ranges = [
        [int(low), int(high)] for low, high in 
        [r.split('-') for r in f.read().splitlines()]
    ]

MAX_IP = 429_4967_295


ranges.sort()
current_IP = current_max_range = unblocked_IPs = 0
min_IP = None
found = False

for min_, max_ in ranges:
    current_max_range = max(max_, current_max_range)
    
    if min_ > current_IP:
        if not found:
            min_IP = current_IP
            found = True

        unblocked_IPs += min_ - current_IP

    current_IP = current_max_range + 1

print(f'Part 1: {min_IP}') # 14975795 - part 1

print(f'Part 2: {unblocked_IPs}') # 101 - part 2
