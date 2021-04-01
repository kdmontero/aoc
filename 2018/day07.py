import heapq

print('Advent of Code 2018 - Day 07')
with open('day07.txt') as f:
    letters = set()
    nodes_before = {}
    nodes_after = {}
    for line in f.read().splitlines():
        node_1, node_2 = list(line.replace('Step ', '').replace(
            ' must be finished before step ','').replace(
            ' can begin.', ''))

        letters.add(node_1)
        letters.add(node_2)

        if node_1 not in nodes_after:
            nodes_after[node_1] = [node_2]
            heapq.heapify(nodes_after[node_1])
        else:
            heapq.heappush(nodes_after[node_1], node_2)

        if node_2 not in nodes_before:
            nodes_before[node_2] = [node_1]
            heapq.heapify(nodes_before[node_2])
        else:
            heapq.heappush(nodes_before[node_2], node_1)

available_nodes = list(letters - nodes_before.keys())
heapq.heapify(available_nodes)

# part 1
order = ''
available_nodes1 = available_nodes[:]

while set(order) != letters:
    current_node = heapq.heappop(available_nodes1)
    order += current_node

    if current_node not in nodes_after:
        continue

    for next_node in nodes_after[current_node]:
        for prereq in nodes_before[next_node]:
            if prereq not in order:
                break
        else:
            heapq.heappush(available_nodes1, next_node)

print(f'Part 1: {order}') # PFKQWJSVUXEMNIHGTYDOZACRLB


# part 2
OFFSET = 60
NO_OF_WORKERS = 5

class Worker:
    def __init__(self):
        self.work = None
        self.timer = None
        self.is_idle = True

    def start_work(self, letter):
        self.work = letter
        self.is_idle = False
        self.timer = OFFSET + ord(letter) - 64 # 64 = ord('A') - 1

    def stop_work(self):
        self.__init__()

    def __str__(self):
        return (f'{self.work}, {self.timer}, {self.is_idle}')

    __repr__ = __str__
    
order = ''
available_nodes2 = available_nodes[:]
time = 0
workers = [Worker() for _ in range(NO_OF_WORKERS)]

while True:
    for worker in workers:
        if worker.timer == 0:
            order += worker.work

            if worker.work in nodes_after:
                for next_node in nodes_after[worker.work]:
                    for prereq in nodes_before[next_node]:
                        if prereq not in order:
                            break
                    else:
                        heapq.heappush(available_nodes2, next_node)

            worker.stop_work()

    if set(order) == letters:
        break

    for worker in workers:
        if worker.is_idle and available_nodes2:
            worker.start_work(heapq.heappop(available_nodes2))

    time += 1
    for worker in [worker for worker in workers if worker.is_idle == False]:
        worker.timer -= 1

print(f'Part 2: {time}') # 864 with order PQWFKJSVXUYEMZDNIHTAGOCRLB
