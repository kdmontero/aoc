if __name__ == '__main__':
    print("Advent of Code 2018 - Day 25: Four-Dimensional Adventure")

    with open('day25.txt') as f:
        stars = []
        for line in f.read().strip().splitlines():
            coords = [int(num) for num in line.split(',')]
            stars.append(coords)

    def check(star: list[int], other_star: list[int]) -> bool:
        distance = 0
        for coord1, coord2 in zip(star, other_star):
            distance += abs(coord1 - coord2)
        return distance <= 3

    constellations = []
    for star in stars:
        far_constellations = []
        member_constellation = []
        for constellation in constellations:
            is_part = False
            for other_star in constellation:
                if check(star, other_star):
                    is_part = True
                    break
            if is_part:
                member_constellation.extend(constellation)
            else:
                far_constellations.append(constellation)

        member_constellation.append(star)
        constellations = [member_constellation] + far_constellations


    print(f'Part 1: {len(constellations)}') # 425

    print(f'Part 2: Complete all 49 stars in Advent of Code 2018')

