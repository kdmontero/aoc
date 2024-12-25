if __name__ == '__main__':
    print("Advent of Code 2017 - Day 20: Particle Swarm")

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
    shortest_a_vector = 100000000000
    shortest_v_vector = 100000000000
    shortest_p_vector = 100000000000
    a_sort_particles = []
    v_sort_particles = []
    p_sort_particles = []

    for particle, a in a_dict.items():
        a_vector = (a[0]**2 + a[1]**2 + a[2]**2)**0.5
        if a_vector < shortest_a_vector:
            a_sort_particles = [particle]
            shortest_a_vector = a_vector
        elif a_vector == shortest_a_vector:
            a_sort_particles.append(particle)

    for particle in a_sort_particles:
        v = v_dict[particle]
        v_vector = (v[0]**2 + v[1]**2 + v[2]**2)**0.5
        if v_vector < shortest_v_vector:
            v_sort_particles = [particle]
            shortest_v_vector = v_vector
        elif v_vector == shortest_v_vector:
            v_sort_particles.append(particle)

    for particle in v_sort_particles:
        p = p_dict[particle]
        p_vector = (p[0]**2 + p[1]**2 + p[2]**2)**0.5
        if p_vector < shortest_p_vector:
            p_sort_particles = [particle]
            shortest_p_vector = p_vector
        elif p_vector == shortest_p_vector:
            p_sort_particles.append(particle)

    print(f'Part 1: {p_sort_particles[0]}') # 91
