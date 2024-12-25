import hashlib
import collections

print("Advent of Code 2016 - Day 14: One-Time Pad")
INPUT = 'qzyelonm'

def get_hash(salt, num, repeat):
    value = salt + str(num)
    for _ in range(repeat):
        md5_hash = hashlib.md5(value.encode()).hexdigest()
        value = md5_hash
    return md5_hash

def has_three(md5_hash):
    for i in range(len(md5_hash)-2):
        if md5_hash[i] == md5_hash[i+1] == md5_hash[i+2]:
            char = md5_hash[i]
            return char
    return False

def has_five(md5_hash):
    fives = set()
    for i in range(len(md5_hash)-4):
        for r in range(1, 5):
            if md5_hash[i] != md5_hash[i+r]:
                break
        else:
            fives.add(md5_hash[i])
    return fives

def find_key(salt, repeat):
    key = 0
    count = 0
    queue = collections.deque()
    triple = {}
    quintet = {}
    hashes = {}

    while count < 64:
        if not queue:
            key += 1
            if key not in hashes:
                key_hash = get_hash(salt, key, repeat)
                hashes[key] = key_hash
            else:
                key_hash = hashes[key]
            char = has_three(key_hash)
            if not char:
                continue
        else:
            key = queue.popleft()
            char = triple[key]

        for index in range(key+1, key + 1001):
            if index not in hashes:
                index_hash = get_hash(salt, index, repeat)
                hashes[index] = index_hash
            else:
                index_hash = hashes[index]

            triple_char = has_three(index_hash)
            if (triple_char) and (index not in queue):
                queue.append(index)
                triple[index] = triple_char

            if index in quintet:
                check = quintet[index]
            else:
                check = has_five(index_hash)
                quintet[index] = check

            if char in check:
                value = salt + str(index)
                count += 1
                break
        else:
            key = index

    return key

print(f'Part 1: {find_key(INPUT, 1)}') # 15168 - part 1

print(f'Part 2: {find_key(INPUT, 2017)}') # 20864 - part 2
