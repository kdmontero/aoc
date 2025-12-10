from collections import defaultdict
from itertools import combinations


if __name__ == '__main__':
    print("Advent of Code 2025 - Day 08: Playground")

    BoxCoord = tuple[int, int, int]
    BoxPairCoords = tuple[BoxCoord, BoxCoord]

    with open('day08.txt') as f:
        boxes: set[BoxCoord] = set()
        for line in f.read().strip().splitlines():
            x, y, z = line.strip().split(',')
            boxes.add((int(x), int(y), int(z)))

    def get_distance(
        box1: BoxCoord,
        box2: BoxCoord
    ) -> int:
        x1, y1, z1 = box1
        x2, y2, z2 = box2

        return (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2

    distances_map: dict[int, list[BoxPairCoords]] = defaultdict(list)
    distances_set: set[int] = set()

    for box1, box2 in combinations(boxes, 2):
        distance = get_distance(box1, box2)
        distances_map[distance].append((box1, box2))
        distances_set.add(distance)

    sorted_distances: list[int] = sorted(list(distances_set))
    sorted_pairs: list[BoxPairCoords] = []
    for distance in sorted_distances:
        sorted_pairs += distances_map[distance]

    circuits: list[set[BoxCoord]] = []
    for i, (box1, box2) in enumerate(sorted_pairs):
        boxes -= {box1, box2}

        circuit1 = None
        for circuit in circuits:
            if box1 in circuit:
                circuit1 = circuit
                break

        circuit2 = None
        for circuit in circuits:
            if box2 in circuit:
                circuit2 = circuit
                break

        if circuit1 == circuit2 == None:
            circuits.append({box1, box2})
        elif circuit1 == circuit2:
            pass
        elif circuit1 is not None and circuit2 is None:
            circuit1.add(box2)
        elif circuit1 is None and circuit2 is not None:
            circuit2.add(box1)
        else: # both are not None and has different circuits
            circuit1 |= circuit2
            circuit2_index = circuits.index(circuit2)
            del circuits[circuit2_index]

        if i == 999:
            circuits.sort(key=lambda a: len(a), reverse=True)
            big_3_product = len(circuits[0]) * len(circuits[1]) * len(circuits[2])

        if len(circuits) == 1 and boxes == set():
            x1, x2 = box1[0], box2[0]
            junction_boxes_product = x1 * x2
            break
            

    print(f'Part 1: {big_3_product}') # 164475

    print(f'Part 2: {junction_boxes_product}') # 169521198

