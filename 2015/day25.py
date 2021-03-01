print('Advent of Code 2015 - Day 25')
given = 'To continue, please consult the code grid in the manual.  Enter the code at row 2978, column 3083.'

# part 1
ROW = 2_978
COL = 3_083
MULT = 252_533
DIV = 33_554_393
height = ROW + COL - 2
i = ((height * (height + 1)) // 2) + COL
code = 20151125
for _ in range(i-1):
    code = (code * MULT) % DIV

print(f'Part 1: {code}') # 2650453

# part 2
print('Part 2: Complete all 49 stars in Advent of Code 2015')
