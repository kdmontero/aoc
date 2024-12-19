import re
import numpy as np


if __name__ == '__main__':
    print('Advent of Code 2024 - Day 13: Claw Contraption')

    with open('day13.txt') as f:
        button_as = []
        button_bs = []
        prizes1 = []
        prizes2 = []
        p_const = 10_000_000_000_000

        pattern = re.compile(r'X[+=](\d+), Y[+=](\d+)')
        for machine in f.read().strip().split('\n\n'):
            raw_a, raw_b, raw_p = machine.splitlines()
            ax, ay = pattern.findall(raw_a)[0]
            bx, by = pattern.findall(raw_b)[0]
            px, py = pattern.findall(raw_p)[0]
            button_as.append([int(ax), int(ay)])
            button_bs.append([int(bx), int(by)])
            prizes1.append([int(px), int(py)])
            prizes2.append([int(px) + p_const, int(py) + p_const])


    def solve_2_eqn(
        eq1: tuple[int, int, int],
        eq2: tuple[int, int, int]
    ) -> tuple[int, int] | tuple[None, None]:
        '''The integer inputs of equations `eq1` and `eq2` are the
        coefficients A, B, C respectively in the form Ax + By = C.
        The return value is the solution (x, y).

        Example:
        eq1: x - 2y = -4
        eq2: 5x + 3y = 19
        solution: x = 2, y = 3

        solve_2_eqn((1, -2, -4), (5, 3, 19)) -> (2, 3)
        '''
        a1, b1, c1 = eq1
        a2, b2, c2 = eq2

        arr = np.array([
            [a1, b1],
            [a2, b2]
        ])
        const = np.array([c1, c2])

        solution = np.linalg.solve(arr, const)
        x = solution[0].round().astype(int)
        y = solution[1].round().astype(int)

        # check the integer solution
        if a1*x + b1*y == c1 and a2*x + b2*y == c2:
            return (x, y)

        return (None, None)


    def get_tokens(prizes: tuple[int, int]) -> int:
        tokens = 0
        for button_a, button_b, prize in zip(button_as, button_bs, prizes):
            a1, a2 = button_a
            b1, b2 = button_b
            c1, c2 = prize

            eq1 = (a1, b1, c1)
            eq2 = (a2, b2, c2)

            x, y = solve_2_eqn(eq1, eq2)

            if x is not None:
                tokens += x * 3 + y

        return tokens


    print(f'Part 1: {get_tokens(prizes1)}') # 40369

    print(f'Part 2: {get_tokens(prizes2)}') # 72587986598368

