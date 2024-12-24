from collections.abc import Mapping


if __name__ == '__main__':
    print('Advent of Code 2024 - Day 24: Crossed Wires')

    with open('day24.txt') as f:
        raw_states, raw_gates = f.read().strip().split('\n\n')
        orig_states = {}
        for state in raw_states.splitlines():
            var, value = state.split(': ')
            orig_states[var] = int(value)

        orig_gates = {}
        for gate in raw_gates.splitlines():
            input1, logic, input2, output = gate.replace('-> ', '').split()
            orig_gates[output] = (logic, input1, input2)

    def get_value(
        node: str,
        states: Mapping[str, int],
        gates: Mapping[str, tuple[str, int, int]]
    ) -> int:

        if node in states:
            return states[node]

        logic, input1, input2 = gates[node]

        input1_value = get_value(input1, states, gates)
        input2_value = get_value(input2, states, gates)
        if logic == 'AND':
            output = int(input1_value and input2_value)
        elif logic == 'OR':
            output = int(input1_value or input2_value)
        elif logic == 'XOR':
            output = int(input1_value ^ input2_value)

        states[node] = output
        return output


    def run_device(
        states: Mapping[str, int],
        gates: Mapping[str, tuple[str, int, int]]
    ) -> int:

        z_list = []
        for node in gates:
            if node.startswith('z'):
                z_list.append([node, get_value(node, states, gates)])

        z_list.sort(key=lambda x:x[0], reverse=True)

        binary_z = ''
        for _, val in z_list:
            binary_z += str(val)

        return int(binary_z, 2)

    dec_z = run_device(orig_states, orig_gates)

    print(f'Part 1: {dec_z}') # 38869984335432


    # part 2

    print(f'Part 2: {0}') #

