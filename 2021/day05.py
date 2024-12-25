from collections import Counter

if __name__ == '__main__':
    print("Advent of Code 2021 - Day 05: Hydrothermal Venture")

    with open('day05.txt') as f:
        vent_points = []
        for line in f.read().splitlines():
            line = line.replace(' -> ',',')
            vent_points.append([int(i) for i in line.split(',')])

    # part 1

    def overlap_counter1(points): # for vertical and horizontal only
        overlap = Counter()

        for x1, y1, x2, y2 in points:
            if x1 == x2:
                min_y = min(y1, y2)
                max_y = max(y1, y2)

                for y in range(min_y, max_y+1):
                    overlap[(x1, y)] += 1
            
            elif y1 == y2:
                min_x = min(x1, x2)
                max_x = max(x1, x2)

                for x in range(min_x, max_x+1):
                    overlap[(x, y1)] += 1

        return overlap


    def count_overlap(counter):
        overlap_points = 0
        for i in counter.values():
            if i > 1:
                overlap_points += 1

        return overlap_points

    vent_points1 = [] # horizontal or vertical only
    for x1, y1, x2, y2 in vent_points:
        if (x1 == x2) or (y1 == y2):
            vent_points1.append([x1, y1, x2, y2])

    counter = overlap_counter1(vent_points1)
    answer1 = count_overlap(counter)

    print(f'Part 1: {answer1}') # 3990


    # part 2

    def overlap_counter2(points): # for diagonal only
        overlap = Counter()

        for x1, y1, x2, y2 in points:
            if x2 < x1:
                x1, y1, x2, y2 = x2, y2, x1, y1

            if y2 > y1:
                slope = 1
            else:
                slope = -1

            for x, y in zip(range(x1, x2+1), range(y1, y2+slope, slope)):
                overlap[(x, y)] += 1

        return overlap
    
    vent_points2 = [] # diagonal only
    for x1, y1, x2, y2 in vent_points:
        if (abs(x1 - x2) == abs(y1 - y2)) and (x1 != x2):
            vent_points2.append([x1, y1, x2, y2])
    
    counter.update(overlap_counter2(vent_points2))
    answer2 = count_overlap(counter)

    print(f'Part 2: {answer2}') # 21305
