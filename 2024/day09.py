from __future__ import annotations


class FileBlock:
    def __init__(self, index: int, id: int, length: int) -> None:
        self.index: int = index
        self.id: int = id
        self.length: int = length
        self.forward: FileBlock = None # FileBlock after self
        self.back: FileBlock = None # FileBlock before self

    def connect_forward(self, other: FileBlock | None) -> None:
        if other is not None:
            self.forward = other
            other.back = self

class LinkedList:
    def __init__(self, root: FileBlock | None = None) -> None:
        self.root = root
        self.leaf = root

    def add_node(self, node: FileBlock) -> None:
        if self.leaf is not None:
            self.leaf.connect_forward(node)
            self.leaf = node
        else:
            self.root = node
            self.leaf = node

    def print_list(self):
        cur = self.root
        while cur is not None:
            print(f'index={cur.index}, id={cur.id}, len={cur.length}')
            cur = cur.forward

    def to_list(self) -> list:
        new_list = []
        cur = self.root
        while cur is not None:
            new_list += [cur.id] * cur.length
            cur = cur.forward
        return new_list
    

if __name__ == '__main__':
    print("Advent of Code 2024 - Day 09: Disk Fragmenter")

    with open('day09.txt') as f:
        disk_map = [int(num) for num in f.read().strip()]


    def checksum(filesystem: list[int]) -> int:
        total_checksum = 0
        for i, num in enumerate(filesystem):
            if num is not None:
                total_checksum += i * num
        return total_checksum


    # part 1

    disk = []
    is_file = True
    compressed_len = 0
    for id, num in enumerate(disk_map):
        if is_file:
            disk += [id//2] * num
            compressed_len += num
        else:
            disk += [None] * num
        is_file = not is_file

    compressed_disk = disk[:compressed_len]
    excess_block = [i for i in disk[compressed_len:] if i is not None]

    for i, space in enumerate(compressed_disk):
        if space is None:
            compressed_disk[i] = excess_block.pop()

    print(f'Part 1: {checksum(compressed_disk)}') # 6432869891895


    # part 2

    disk_layout = LinkedList()
    valid_file_blocks = []
    index = 0
    is_file = True
    for id, num in enumerate(disk_map):
        if is_file:
            file_block = FileBlock(index, id//2, num)
            valid_file_blocks.append(file_block)
        else:
            file_block = FileBlock(index, None, num)

        # (index of the first file in the block, id, file block length)
        disk_layout.add_node(file_block) 

        index += num
        is_file = not is_file

    while valid_file_blocks:
        cur_file = valid_file_blocks.pop()
        cur_node = disk_layout.root

        while cur_file.index > cur_node.index:
            # if space is found
            if cur_node.id is None and cur_node.length >= cur_file.length:

                # replace the current file with space
                space = FileBlock(cur_file.index, None, cur_file.length)
                cur_file.back.connect_forward(space)
                space.connect_forward(cur_file.forward)

                # re-index the file and the node
                cur_file.index = cur_node.index
                cur_node.index = cur_file.index + cur_file.length

                # move the file block
                cur_node.back.connect_forward(cur_file)
                cur_file.connect_forward(cur_node)

                # reduce the length of file space
                cur_node.length -= cur_file.length

            cur_node = cur_node.forward

    print(f'Part 2: {checksum(disk_layout.to_list())}') # 6467290479134

