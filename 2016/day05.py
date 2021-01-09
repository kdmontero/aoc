import hashlib

INPUT = 'ojvtpuvg'

# part 1
door_id = INPUT
ZEROES = 5
password1 = ''
i = 0
while len(password1) < 8:
    value = door_id + str(i)
    md5_hash = hashlib.md5(value.encode()).hexdigest()
    if md5_hash.startswith('0'*ZEROES):
        password1 += md5_hash[ZEROES]
    i += 1

print(f'Part 1: {password1}') # 4543c154


# part 2
password2 = [' '] * 8
i = 0
while ' ' in password2:
    value = door_id + str(i)
    md5_hash = hashlib.md5(value.encode()).hexdigest()
    if (md5_hash.startswith('0'*ZEROES) and
        '0' <= md5_hash[ZEROES] <= '7'):
            if password2[int(md5_hash[ZEROES])] == ' ':
                password2[int(md5_hash[ZEROES])] = md5_hash[ZEROES+1]    
    i += 1

print(f'Part 2: {"".join(password2)}') # 1050cbbd