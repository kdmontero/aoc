from __future__ import annotations


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.before: Node = self
        self.after: Node = self

    def connect_right(self, other: Node) -> None:
        '''From: node_x --> self --> node_y
        To: node_x --> self --> other --> node_y
        '''
        node_y = self.after
        self.after, other.before = other, self
        other.after = node_y
        node_y.before = other

    def connect_left(self, other: Node) -> None:
        '''From: node_x --> self --> node_y
        To: node_x --> other --> self --> node_y
        '''
        node_x = self.before
        self.before, other.after = other, self
        other.before = node_x
        node_x.after = other

    def remove(self) -> None:
        self.before.after = self.after
        self.after.before = self.before

    def traverse_right(self, steps: int) -> Node:
        cur_node = self
        for _ in range(steps):
            cur_node = cur_node.after
        return cur_node

    def traverse_left(self, steps: int) -> Node:
        cur_node = self
        for _ in range(steps):
            cur_node = cur_node.before
        return cur_node

    def print_loop(self, length: int) -> None:
        node = self
        loop = []
        for _ in range(length):
            loop.append(node)
            node = node.after
        print(loop)

    def __str__(self) -> str:
        return f'{self.val}'

    __repr__ = __str__


if __name__ == '__main__':
    print("Advent of Code 2022 - Day 20: Grove Positioning System")

    with open('day20.txt') as f:
        nums = [int(num) for num in f.read().strip().splitlines()]

    def generate_orig_file(nums: list[int]) -> list[Node]:
        file = []
        cur_node = Node(0)
        for num in nums:
            node = Node(num)
            file.append(node)
            cur_node.connect_right(node)
            cur_node = node
        cur_node.after.remove()

        return file

    def mix(node: Node, length: int) -> None:
        move = (abs(node.val) % (length - 1))
        if move == 0:
            return

        if node.val > 0:
            target_node = node.traverse_right(move)
            node.remove()
            target_node.connect_right(node)
        elif node.val < 0:
            target_node = node.traverse_left(move)
            node.remove()
            target_node.connect_left(node)

    def mix_file(file: list[Node], rounds: int) -> int:

        for node in file:
            if node.val == 0:
                node_zero = node
                break

        length = len(file)
        for _ in range(rounds):
            for node in file:
                mix(node, length)

        total = 0
        for i in [1000, 2000, 3000]:
            total += node_zero.traverse_right(i % length).val

        return total
        

    # part 1

    file1 = generate_orig_file(nums)
    groove_total1 = mix_file(file1, 1)
    print(f'Part 1: {groove_total1}') # 11073


    # part 2

    file2 = generate_orig_file(nums)
    for node in file2:
        node.val = node.val * 811589153

    groove_total2 = mix_file(file2, 10)
    print(f'Part 2: {groove_total2}') # 11102539613040

