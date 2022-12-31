from __future__ import annotations

class Node:
    def __init__(self, n_child: int, n_meta: int) -> None:
        self.n_child = n_child
        self.n_meta = n_meta
        self.meta: list[int] = []
        self.child: list[Node] = []
        self.parent: Node = None

    def __str__(self) -> None:
        return f'Node(node={self.n_child}, meta={self.n_meta})'

    __repr__ = __str__


if __name__ == '__main__':
    print('Advent of Code 2018 - Day 08')

    with open('day08.txt') as f:
        data = [int(num) for num in f.read().split()]

    def form_tree(node: Node, data: list[int]) -> list[int]:

        if data == []:
            return 

        if len(node.child) == node.n_child and len(node.meta) == node.n_meta:
            return data

        if len(node.child) < node.n_child:
            child_node = Node(data[0], data[1])
            node.child.append(child_node)
            child_node.parent = node
            new_data = form_tree(child_node, data[2:])
            return form_tree(node, new_data)

        if len(node.meta) < node.n_meta:
            node.meta.append(data[0])
            return form_tree(node, data[1:])


    # part 1

    root = Node(data[0], data[1])
    form_tree(root, data[2:])

    def get_all_meta(node: Node, meta_total) -> int:
        if not node.child:
            return sum(node.meta)

        for c_node in node.child:
            meta_total += get_all_meta(c_node, sum(c_node.meta))

        return meta_total
            
    print(f'Part 1: {get_all_meta(root, sum(root.meta))}') # 35852


    # part 2

    def get_all_values(node: Node, values_total) -> int:
        if not node.child:
            return sum(node.meta)

        for i in node.meta:
            if i > len(node.child):
                values_total += 0
            else:
                values_total += get_all_values(node.child[i-1], 0)

        return values_total

    print(f'Part 2: {get_all_values(root, 0)}') # 33422
