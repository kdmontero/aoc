from collections import Counter

print("Advent of Code 2019 - Day 12: The N-Body Problem")
with open('day12.txt') as f:
    given_pos = [
        line.strip('>').replace('<x=', '').replace('y=', '').replace(
        'z=', '').split(', ') for line in f.read().splitlines()
    ]

moons_pos = [[int(num) for num in axis] for axis in zip(*given_pos)] 
# pos per coordinates [[x1, x2, x3, x4], [y1, y2, y3, y4],.. ]
moons_vel = [[0] * len(moons_pos[0]) for _ in range(len(moons_pos))]
# vel per coordinates [[x1, x2, x3, x4], [y1, y2, y3, y4],.. ]

# part 1
def get_gravity(axis_pos):
    axis_grav = []
    for moon in axis_pos:
        grav = 0
        for other in axis_pos:
            if moon is not other and moon < other:
                grav += 1
            elif moon is not other and moon > other:
                grav -= 1
        axis_grav.append(grav)
    return axis_grav

def get_velocity(axis_vel: list, axis_grav):
    return [sum(values) for values in zip(axis_vel, axis_grav)]

def get_position(axis_pos, axis_vel):
    return [sum(values) for values in zip(axis_pos, axis_vel)]

def get_energy(pos, vel):
    potential = [abs(i) for i in pos]
    kinetic = [abs(i) for i in vel]
    return sum(potential) * sum(kinetic)

for step in range(1000):
    moons_grav = [get_gravity(pos) for pos in moons_pos]
    # grav per coordinates [[x1, x2, x3, x4], [y1, y2, y3, y4],.. ]
    moons_vel = [get_velocity(vel, grav) for vel, grav in zip(moons_vel, moons_grav)]
    moons_pos = [get_position(pos, vel) for pos, vel in zip(moons_pos, moons_vel)]

positions = list(zip(*moons_pos)) # pos per moon [(x1, y1, z1) ,(x2, y2, z2),...]
velocities = list(zip(*moons_vel)) # vel per moon [(x1, y1, z1) ,(x2, y2, z2),...]
moons = list(zip(positions, velocities)) 
# pos and vel per moon -> list of tuples of tuples of int

total_energy = 0
for moon in moons:
    total_energy += get_energy(*moon)

print(f'Part 1: {total_energy}') # 7928


# part 2
def get_revolution(axis_pos, axis_vel):
    init_pos = axis_pos[:]
    step = 1
    while True:
        axis_grav = get_gravity(axis_pos)
        axis_vel = [sum(i) for i in zip(axis_vel, axis_grav)]
        axis_pos = [sum(i) for i in zip(axis_pos, axis_vel)]
        step += 1
        if axis_pos == init_pos:
            return step

def get_prime_factors(num):
    prime_factors = Counter()
    i = 2
    while i <= num:
        if num % i == 0:
            prime_factors[i] += 1
            num = num // i
        else:
            i += 1
    return prime_factors

def get_lcm(nums):
    factors = Counter()
    for num in nums:
        factors |= get_prime_factors(num) # union of Counters
    lcm = 1
    for factor, exp in factors.items():
        lcm *= factor**exp
    return lcm

moons_pos = [[int(num) for num in axis] for axis in zip(*given_pos)]
moons_vel = [[0] * len(moons_pos[0]) for _ in range(len(moons_pos))]

axis_revs = []
for axis_pos, axis_vel in zip(moons_pos, moons_vel):
    axis_revs.append(get_revolution(axis_pos, axis_vel))

print(f'Part 2: {get_lcm(axis_revs)}') # 518311327635164
