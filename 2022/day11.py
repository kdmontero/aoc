from collections import deque
import copy

class Monkey:
    monkey = {}

    def __init__(
        self,
        number: int,
        items: deque,
        operation: str,
        test: int,
        true: int,
        false: int
    ) -> None:
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.count = 0


    def __str__(self) -> None:
        return f'Monkey({self.number}, test: {self.test}, count: {self.count})'

    __repr__ = __str__


    def test_item(self, item: int) -> bool:
        return True if item % self.test == 0 else False


    def inspect(self, item: int) -> int:
        old = item
        return eval(self.operation)


if __name__ == '__main__':
    print("Advent of Code 2022 - Day 11: Monkey in the Middle")

    with open('day11.txt') as f:
        for str_block in f.read().split('\n\n'):
            for line in str_block.splitlines():
                line = line.strip()
                if line.startswith('Monkey'):
                    monkey_num = int(line.replace(':','').split()[1])
                if line.startswith('Starting items'):
                    items = deque([int(num) for num in 
                        line.replace('Starting items: ','').split(', ')
                    ])
                if line.startswith('Operation: '):
                    operation = line.replace('Operation: new = ', '')
                if line.startswith('Test: '):
                    test = int(line.split()[-1])
                if line.startswith('If true:'):
                    true = int(line.split()[-1])
                if line.startswith('If false:'):
                    false = int(line.split()[-1])

            Monkey.monkey[monkey_num] = Monkey(
                monkey_num,
                items,
                operation,
                test,
                true,
                false
            )

    # part 1
    
    monkey1 = copy.deepcopy(Monkey.monkey)
    for _ in range(20):
        for i in range(len(monkey1)):
            while monkey1[i].items:
                item = monkey1[i].items.popleft()
                old = item
                item = eval(monkey1[i].operation)
                item = item // 3
                if monkey1[i].test_item(item):
                    monkey1[monkey1[i].true].items.append(item)
                else:
                    monkey1[monkey1[i].false].items.append(item)
                monkey1[i].count += 1


    monkey_counts1 = []
    for m in monkey1.values():
        monkey_counts1.append(m.count)
    monkey_counts1.sort(reverse=True)

    print(f'Part 1: {monkey_counts1[0] * monkey_counts1[1]}') # 119715


    # part 2

    monkey2 = copy.deepcopy(Monkey.monkey)

    mod_all = 1
    for m in monkey2.values():
        mod_all *= m.test

    for _ in range(10000):
        for i in range(len(monkey2)):
            while monkey2[i].items:
                item = monkey2[i].items.popleft()
                old = item
                item = eval(monkey2[i].operation)
                item = item % mod_all
                if monkey2[i].test_item(item):
                    monkey2[monkey2[i].true].items.append(item)
                else:
                    monkey2[monkey2[i].false].items.append(item)
                monkey2[i].count += 1


    monkey_counts2 = []
    for m in monkey2.values():
        monkey_counts2.append(m.count)
    monkey_counts2.sort(reverse=True)

    print(f'Part 2: {monkey_counts2[0] * monkey_counts2[1]}') # 18085004878
