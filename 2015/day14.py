print("Advent of Code 2015 - Day 14: Reindeer Olympics")
class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.status = 'rest' # 'rest' or 'fly'
        self.time_remaining = 0
        self.distance = 0
        self.points = 0

    def after_one_sec(self):
        if self.time_remaining > 0:
            if self.status == 'fly':
                self.distance += self.speed
        else:
            if self.status == 'rest':
                self.status = 'fly'
                self.distance += self.speed
                self.time_remaining = self.fly_time
            elif self.status == 'fly':
                self.status = 'rest'
                self.time_remaining = self.rest_time
        self.time_remaining -= 1
    
    def __lt__(self, other):
        return True if self.distance < other.distance else False
    
    def __gt__(self, other):
        return True if self.distance > other.distance else False    

    def __eq__(self, other):
        return True if self.distance == other.distance else False    

with open('day14.txt') as f:
    reindeers = []
    for line in f.read().splitlines():
        line = line.replace('can fly ', '').replace('km/s for ','').replace(
            'seconds, but then must rest for ', '').replace(' seconds.','')
        name, speed, fly_time, rest_time = line.split(' ')
        reindeer = Reindeer(name, int(speed), int(fly_time), int(rest_time))
        reindeers.append(reindeer)

FINISH = 2503
time = 0
while time < FINISH:
    for reindeer in reindeers:
        reindeer.after_one_sec()
    max_distance = max([reindeer.distance for reindeer in reindeers])
    for reindeer in reindeers:
        if reindeer.distance == max_distance:
            reindeer.points += 1
    time += 1

# part 1
max_distance = max([reindeer.distance for reindeer in reindeers])
print(f'Part 1: {max_distance}') # 2660


# part 2
max_points = max([reindeer.points for reindeer in reindeers])
print(f'Part 2: {max_points}') # 1256
