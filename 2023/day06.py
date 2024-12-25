import math


if __name__ == '__main__':
    print("Advent of Code 2023 - Day 06: Wait For It")

    with open('day06.txt') as f:
        records = []
        one_time = ''
        one_distance = ''
        times, distances = f.read().splitlines()
        for i, (t, d) in enumerate(zip(times.split(), distances.split())):
            if i == 0:
                continue
            records.append([int(t), int(d)]) 
            one_time += t
            one_distance += d

    # solve in O(1) using quadratic equation
    def ways_to_beat(time: int, distance: int) -> int:
        x1 = math.ceil((-time + (time**2 - (4*distance))**0.5)/-2)
        x2 = math.floor((-time - (time**2 - (4*distance))**0.5)/-2)
        return x2 - x1 + 1


    # part 1

    margin_of_error = 1
    for time, distance in records:
        margin_of_error *= ways_to_beat(time, distance)
    
    print(f'Part 1: {margin_of_error}') # 861300


    # part 2
    
    winning_scenarios = ways_to_beat(int(one_time), int(one_distance))

    print(f'Part 2: {winning_scenarios}') # 28101347