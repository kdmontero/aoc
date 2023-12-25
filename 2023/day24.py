import numpy as np
import z3


if __name__ == '__main__':
    print('Advent of Code 2023 - Day 24')

    with open('day24.txt') as f:
        records = []
        for line in f.read().splitlines():
            pos, vel = line.split(' @ ')
            px, py, pz = [int(num) for num in pos.split(', ')]
            vx, vy, vz = [int(num) for num in vel.split(', ')]
            records.append([px, py, pz, vx, vy, vz])

    # part 1
    def check_future_pos(
        px: int, py: int, 
        vx: int, vy: int, 
        ix: int, iy: int
    ) -> bool:
        if (ix - px) * vx < 0:
            return False
        if (iy - py) * vy < 0:
            return False
        return True

    def find_intersection(point1: list[int], point2: list[int]) -> list[int]:
        x1, y1, vx1, vy1 = point1
        x2, y2, vx2, vy2 = point2
        arr = np.array([[vy1, -vx1], [vy2, -vx2]])
        const = np.array([
            vy1 * x1 - vx1 * y1, 
            vy2 * x2 - vx2 * y2
        ])
        if np.linalg.det(arr) == 0:
            return -1, -1
        ix, iy = np.linalg.solve(arr, const)
        return ix, iy

    collision = 0
    for i, obj1 in enumerate(records[:-1]):
        for obj2 in records[i+1:]:
            x1, y1, _, vx1, vy1, _ = obj1
            x2, y2, _, vx2, vy2, _ = obj2
            ix, iy = find_intersection([x1, y1, vx1, vy1], [x2, y2, vx2, vy2])
            if all((
                (200000000000000 < ix < 400000000000000),
                (200000000000000 < iy < 400000000000000),
                check_future_pos(x1, y1, vx1, vy1, ix, iy),
                check_future_pos(x2, y2, vx2, vy2, ix, iy)
            )):
                collision += 1

    print(f'Part 1: {collision}') # 15558


    # part 2
    px1, py1, pz1, xv1, yv1, zv1 = records[0]
    px2, py2, pz2, xv2, yv2, zv2 = records[1]
    px3, py3, pz3, xv3, yv3, zv3 = records[2]

    # collision times for 3 hails
    t, u, v = z3.Real('t'), z3.Real('u'), z3.Real('v')

    # position of the rock in x, y, z
    a, b, c = z3.Real('a'), z3.Real('b'), z3.Real('c')

    # velocity of the rock in x, y, z
    i, j, k = z3.Real('i'), z3.Real('j'), z3.Real('k')

    eqns = [
        a + i * t == px1 + xv1 * t,
        b + j * t == py1 + yv1 * t,
        c + k * t == pz1 + zv1 * t,
        a + i * u == px2 + xv2 * u,
        b + j * u == py2 + yv2 * u,
        c + k * u == pz2 + zv2 * u,
        a + i * v == px3 + xv3 * v,
        b + j * v == py3 + yv3 * v,
        c + k * v == pz3 + zv3 * v,
    ]

    s = z3.Solver()
    s.add(*eqns)
    s.check()
    solution = s.model()
    coords_sum = (
        int(solution[a].as_long()) + 
        int(solution[b].as_long()) + 
        int(solution[c].as_long())
    )

    print(f'Part 2: {coords_sum}') # 765636044333842
