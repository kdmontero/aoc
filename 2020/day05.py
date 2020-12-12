with open('day05.txt') as f:
    seats = [seat for seat in f.read().split('\n')]

def row(seat):
    lb = 0
    ub = 128
    mid = (lb + ub)//2
    for char in seat[:7]:
        if char == 'F':
            ub = mid
        elif char == 'B':
            lb = mid
        mid = (lb + ub)//2
    return mid

def col(seat):
    lb = 0
    ub = 8
    mid = (lb + ub)//2
    for char in seat[7:]:
        if char == 'L':
            ub = mid
        elif char == 'R':
            lb = mid
        mid = (lb + ub)//2
    return mid

# part 1
max_id = 0
seat_dict = {}
for seat in seats:
    seat_id = row(seat) * 8 + col(seat)
    max_id = max(max_id, seat_id)
    seat_dict[(row(seat), col(seat))] = seat_id

print(f'Part 1: {max_id}') # 955


# part 2
def check_seat(seat_id):
    for row in range(1, 127):
        col = seat_id - (row * 8)
        if not (0 <= col <= 7):
            continue
        if (row, col) not in seat_dict:
            return True
    return False

my_id = None
for seat, seat_id in seat_dict.items():
    if (seat_id+2 in seat_dict.values()) and check_seat(seat_id+1):
        my_id = seat_id+1
        break
    if (seat_id-2 in seat_dict.values()) and check_seat(seat_id-1):
        my_id = seat_id-1
        break

print(f'Part 2: {my_id}') # 569