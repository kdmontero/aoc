if __name__ == '__main__':
    print('Advent of Code 2017 - Day 20')

    with open('day20.txt') as f:
        p_dict = {}
        v_dict = {}
        a_dict = {}
        for i, line in enumerate(f.read().splitlines()):
            p, v, a = line.split(', ')
            p_dict[i] = [int(x) for x in p[3:-1].split(',')]
            v_dict[i] = [int(x) for x in v[3:-1].split(',')]
            a_dict[i] = [int(x) for x in a[3:-1].split(',')]


    # part 1
    closest = None
    shortest_a_vector = 100000000000

    for particle, a in a_dict.items():
        a_vector = (a[0]**2 + a[1]**2 + a[2]**2)**0.5
        if a_vector < shortest_a_vector:
            closest = particle
            shortest_a_vector = a_vector

    print(f'Part 1: {closest}') # 91
