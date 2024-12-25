import copy

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_

    def __repr__(self):
        return f'Node({self.value})'

    __str__ = __repr__


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.head.next_ = self.head
        self.length = 1

    def __len__(self):
        return self.length

    def __repr__(self):
        return f'LinkedList({self.head}, {self.length})'

    __str__ = __repr__

    def insert(self, node_before, new_node):
        self.length += 1
        new_node.next_ = node_before.next_
        node_before.next_ = new_node

    @staticmethod
    def move_3_nodes(current, destination):
        '''
        transfers 3 nodes in front (or next) of the current node 
        to the front of destination node

        C - 1 - 2 - 3 - X...D - Y
        '''
        node1 = current.next_
        node3 = node1.next_.next_
        nodeX = node3.next_
        nodeY = destination.next_

        current.next_ = nodeX
        destination.next_ = node1
        node3.next_ = nodeY

    @staticmethod
    def get_node_after(current_node, steps):
        for _ in range(steps):
            current_node = current_node.next_
        return current_node


def print_ll(ll):
    '''for debugging'''
    current = ll.head
    for _ in range(len(ll)):
        print(current)
        current = current.next_


def execute_game(given_circle, rounds, total_cups=0):
    circle = copy.deepcopy(given_circle)
    circle_dict = {}
    current = circle.head
    for _ in range(len(circle)):
        circle_dict[current.value] = current
        current = current.next_

    if total_cups > len(circle):
        i = len(circle)
        current = circle.get_node_after(circle.head, i-1)
        while i < total_cups:
            next_node = Node(i+1)
            circle.insert(current, next_node)
            i += 1
            current = next_node
            circle_dict[i] = current

    current_node = circle.head
    current_value = current_node.value

    for _ in range(rounds):
        three_cups = set()
        h = current_node
        for _ in range(3):
            three_cups.add(h.next_.value)
            h = h.next_


        destination_value = current_value
        while True:
            destination_value -= 1
            if destination_value == 0:
                destination_value = circle.length

            if destination_value not in three_cups:
                break

        destination_node = circle_dict[destination_value]
        circle.move_3_nodes(current_node, destination_node)

        current_node = current_node.next_
        current_value = current_node.value

    return circle, circle_dict


print("Advent of Code 2020 - Day 23: Crab Cups")
given = '538914762'

cups = [int(num) for num in list(given)]
head = Node(cups[0])
circle = LinkedList(head)
current = head
i = 1
while i < len(cups):
    next_node = Node(cups[i])
    circle.insert(current, next_node)
    i += 1
    current = next_node


# part 1

circle1, circle_dict1 = execute_game(circle, 100)
labels = ''
current = circle_dict1[1].next_

while True:
    labels += str(current.value)
    if current.next_.value == 1:
        break
    else:
        current = current.next_
    
print(f'Part 1: {labels}') # 54327968


# part 2

circle2, circle_dict2 = execute_game(circle, 10_000_000, 1_000_000)
cup_a = circle_dict2[1].next_
cup_b = cup_a.next_

print(f'Part 2: {cup_a.value * cup_b.value}') # 157410423276
