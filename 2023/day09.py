if __name__ == '__main__':
    print("Advent of Code 2023 - Day 09: Mirage Maintenance")

    with open('day09.txt') as f:
        report = []
        for line in f.read().splitlines():
            report.append([int(num) for num in line.split()])

    total1 = 0
    total2 = 0
    for values in report:
        levels = [values[:]]
        while True:
            level = []
            for i, num in enumerate(values[1:], 1):
                level.append(num - values[i-1])
            if len(set(level)) == 1:
                extrapolate_end = level[0]
                extrapolate_begin = level[0]
                break
            levels.append(level)
            values = level
        
        for level in levels[::-1]:
            extrapolate_end += level[-1]
            extrapolate_begin = level[0] - extrapolate_begin
        
        total1 += extrapolate_end
        total2 += extrapolate_begin

    print(f'Part 1: {total1}') # 2175229206

    print(f'Part 2: {total2}') # 942