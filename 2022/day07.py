from __future__ import annotations

class Node:

    def __init__(self, name: str, isfolder: bool, size: int=0) -> None:
        self.name = name
        self.isfolder = isfolder
        if self.isfolder:
            self.child: dict[str, Node] | None = {}
            self.size = 0
        else:
            self.child = None
            self.size = size
        self.parent: Node = None

    def add_child(self, child: Node) -> None:
        self.child[child.name] = child
        child.parent = self
        child.update_parent_size()
        
    def update_parent_size(self) -> None:
        current_node = self
        while current_node.parent is not None:
            current_node.parent.size += self.size
            current_node = current_node.parent

            if current_node == self:
                raise AssertionError('Loop is present in the tree')

    def __str__(self) -> None:
        return f'Node({self.name}, {self.isfolder}, {self.size})'

    __repr__ = __str__


if __name__ == '__main__':
    print('Advent of Code 2022 - Day 07')

    with open('day07.txt') as f:
        commands = []
        for line in f.read().splitlines():
            if line.startswith('$'):
                commands.append(line)
            else:
                if isinstance(commands[-1], list):
                    commands[-1].append(line)
                else:
                    commands.append([line])

    # create the file tree

    folders_dict = {}
    root = Node('/', True)
    current_dir = None

    for command in commands:
        if isinstance(command, list):
            for file in command:
                size, filename = file.split()
                if size == 'dir':
                    dirname = current_dir.name + filename + '/'
                    node = Node(dirname, True)
                    folders_dict[dirname] = node
                elif size.isdigit():
                    node = Node(filename, False, int(size))
                current_dir.add_child(node)
        elif command == '$ cd /':
            current_dir = root
        elif command == '$ cd ..':
            current_dir = current_dir.parent
        elif command.startswith('$ cd'):
            inner_dir = current_dir.name + command.split()[2] + '/'
            current_dir = current_dir.child[inner_dir]
        elif command == '$ ls':
            continue

    
    TOTAL_DISK_SPACE = 70_000_000
    SPACE_NEEDED = 30_000_000
    space_to_delete = SPACE_NEEDED - (TOTAL_DISK_SPACE - root.size)

    total_dir_100000 = 0
    smallest_valid_dir = TOTAL_DISK_SPACE

    for dir in folders_dict.values():
        if dir.size <= 100_000:
            total_dir_100000 += dir.size

        if dir.size >= space_to_delete:
            smallest_valid_dir = min(smallest_valid_dir, dir.size)


    print(f'Part 1: {total_dir_100000}') # 1141028 - part 1

    print(f'Part 2: {smallest_valid_dir}') # 8278005 - part 2
