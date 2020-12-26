from copy import deepcopy

class LinkedList:
    instance = False
    first = None
    last = None

    def __init__(self, val):
        self.val = val
        if not self.instance:
            self.next = None
            self.prev = None
            self.seta(self)
            self.change_flag()
        else:
            self.inst(self)
    
    @classmethod
    def change_flag(cls):
        cls.instance = True

    @classmethod
    def inst(cls, self):
        cls.last.connect(self)
        cls.last = self
        cls.last.connect(cls.first) 
    
    @classmethod
    def seta(cls, self):
        cls.first = cls.last = self

    def connect(self, other):
        self.next = other
        other.prev = self
    
    def __str__(self):
        return f'LinkedList {self.val}'

    __repr__ = __str__



giventest = '389125467'
cups = [int(num) for num in list(giventest)]
cups += [num for num in range(10, 1_000_001)]

for num in cups:
    a = LinkedList(num)
    if num == 1:
        head = a

search = 999_990
h = head
n = 0
while True:
    if h.val == search:
        n+=1
        print(n)
    h = h.next
    
