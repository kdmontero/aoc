if __name__ == '__main__':
    print('Advent of Code 2023 - Day 06')

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


    # part 1

    margin_of_error = 1
    for time, distance in records:
        winning_scenarios = 0
        for i in range(1, time + 1):
            if i * (time - i) > distance:
                winning_scenarios += 1
        margin_of_error *= winning_scenarios
    
    print(f'Part 1: {margin_of_error}') # 861300


    # part 2
    
    winning_scenarios = 0
    one_time = int(one_time)
    one_distance = int(one_distance)
    for i in range(1, one_time + 1):
        if i * (one_time - i) > one_distance:
            winning_scenarios += 1
    print(f'Part 2: {winning_scenarios}') # 28101347