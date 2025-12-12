import z3


if __name__ == '__main__':
    print("Advent of Code 2025 - Day 10: Factory")

    with open('day10.txt') as f:
        all_lights: list[str] = []
        all_buttons: list[list[set[int]]] = []
        all_joltages: list[list[int]] = []

        for line in f.read().strip().splitlines():
            lights, *buttons, joltages = line.split(' ')

            all_lights.append(lights[1:-1])

            parsed_buttons: list[set[int]] = []
            for button in buttons:
                parsed_button = [int(b) for b in button[1:-1].split(',')]
                parsed_buttons.append(parsed_button)
            all_buttons.append(parsed_buttons)

            all_joltages.append(
                [int(joltage) for joltage in joltages[1:-1].split(',')]
            )


    # part 1

    def toggle_button(button: set[int], lights: str) -> str:
        lights_list = list(lights)
        for indicator in button:
            state = lights_list[indicator]
            if state == '.':
                lights_list[indicator] = '#'
            elif state == '#':
                lights_list[indicator] = '.'
        return ''.join(lights_list)

    # bfs
    def fewest_press(lights: str, buttons: list[set[int]]) -> int:
        current_state = '.' * len(lights)
        queue: list[str] = [current_state]
        visited: set[str] = set()
        presses = 0
        found = False

        while not found and queue:
            next_queue: list[str] = []

            for current_state in queue:
                if current_state == lights:
                    found = True
                    break
                if current_state in visited:
                    continue

                for button in buttons:
                    next_state = toggle_button(button, current_state)
                    if next_state in visited:
                        continue
                    next_queue.append(next_state)
                visited.add(current_state)

            else:
                queue = next_queue
                presses += 1

        return presses

    total_presses = 0
    for lights, buttons in zip(all_lights, all_buttons):
        total_presses += fewest_press(lights, buttons)

    print(f'Part 1: {total_presses}') # 449


    # part 2

    def solve_counters(joltages: list[int], buttons: list[set[int]]) -> int:
        variables = [z3.Int(f'x{i}') for i in range(len(buttons))]
        opt = z3.Optimize()

        for i, target_joltage in enumerate(joltages):
            total = []
            for var, button in zip(variables, buttons):
                if i in button:
                    total.append(var)
            opt.add(z3.Sum(total) == target_joltage)

        for var in variables:
            opt.add(var >= 0)

        opt.minimize(z3.Sum(variables))

        opt.check()
        solution = opt.model()
        counters = 0

        for var in solution.decls():
            counters += solution[var].as_long()

        return counters

    total_counters = 0
    for joltages, buttons in zip(all_joltages, all_buttons):
        total_counters += solve_counters(joltages, buttons)

    print(f'Part 2: {total_counters}') # 17848

