from collections import deque

class KnotHash:
    STANDARD_LEN_SUFFIX = [17, 31, 73, 47, 23]

    def __init__(self, knot, lengths, skip_size, correction_offset):
        self.knot = knot
        self.lengths = lengths
        self.skip_size = skip_size
        self.correction_offset = correction_offset
    
    @staticmethod
    def get_lengths(string):
        return [ord(char) for char in string] + KnotHash.STANDARD_LEN_SUFFIX
    
    @staticmethod
    def twist(knot, length):
        if length == 0:
            return knot
        sub_knot = list(knot)[length-1::-1]
        knot = sub_knot + list(knot)[length:]
        return deque(knot)

    def knot_hash(self):
        for length in self.lengths:
            self.knot = self.twist(self.knot, length)
            self.knot.rotate(-length-self.skip_size)
            self.correction_offset += length + self.skip_size
            self.skip_size += 1

        self.knot.rotate(self.correction_offset)
        return self.knot[0] * self.knot[1] 
    
    def sparse_hash(self):
        for _ in range(64):
            for length in self.lengths:
                self.knot = self.twist(self.knot, length)
                self.knot.rotate(-length-self.skip_size)
                self.correction_offset += length + self.skip_size
                self.skip_size += 1

        self.knot.rotate(self.correction_offset)

    def dense_hash(self):
        d_hash = []
        for block_start in range(0, 256, 16):
            d_hash_element = 0
            for step in range(16):
                d_hash_element = d_hash_element ^ self.knot[block_start + step]
            d_hash.append(d_hash_element)

        final_dense_hash = ''
        for element in d_hash:
            hex_elem = hex(element)
            if len(hex_elem) < 4:
                final_dense_hash += '0' + hex_elem[-1]
            else:
                final_dense_hash += hex_elem[2:]

        return final_dense_hash

    def final_knot_hash(self):
        self.sparse_hash()
        return self.dense_hash()


if __name__ == '__main__':
    print("Advent of Code 2017 - Day 10: Knot Hash")

    with open('day10.txt') as f:
        given_string = f.read()
        lengths1 = [int(num) for num in given_string.split(',')]

    # part 1
    given = KnotHash(deque(range(256)), lengths1, 0, 0)
    print(f'Part 1: {given.knot_hash()}') # 40132


    # part 2 
    lengths2 = KnotHash.get_lengths(given_string)
    given = KnotHash(deque(range(256)), lengths2, 0, 0)
    print(f'Part 2: {given.final_knot_hash()}') 
    # 35b028fe2c958793f7d5a61d07a008c8
