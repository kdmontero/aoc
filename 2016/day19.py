import collections

INPUT = 3018458

# part 1
exponent = 0
while INPUT > 2**(exponent+1):
    exponent += 1

answer = 1 + 2*(INPUT-2**(exponent))

print(f'Part 1: {answer}') # 1842613


# -------------------- The Josephus Problem Solution --------------------

# Shortcut and clever O(1) solution from Numberphile's youtube video, Josephus
# Problem (https://www.youtube.com/watch?v=uCsD3ZGzMgE&ab_channel=Numberphile)

# def josephus_problem(num):
#     bin_given = bin(num)[2:]
#     bin_answer = bin_given[1:] + bin_given[0] 
#     return int(bin_answer, 2)

# print(f'Part 1: {josephus_problem(INPUT)}') # 1842613

# -----------------------------------------------------------------------


# part 2
circle = collections.deque(range(1, INPUT+1))
circle.rotate(-(INPUT//2))
circle.popleft()

while len(circle) > 1:
    circle.popleft()
    circle.rotate(-1)
    circle.popleft()

print(f'Part 2: {circle.pop()}') # 1424135
