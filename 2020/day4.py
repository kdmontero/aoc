with open('day4.txt') as given:
    passports = []
    pp_details = {}
    for line in given.readlines():
        if line == '\n':
            passports.append(pp_details)
            pp_details = {}
        else:
            fields = line.replace(':', ' ').split(' ')
            for index in range(0, len(fields), 2):
                pp_details[fields[index]] = fields[index+1].rstrip('\n')
    passports.append(pp_details)

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

# part 1 
valid1 = []
for passport in passports:
    pp_fields = set()
    for field in passport:
        pp_fields.add(field)
    if required.issubset(pp_fields):
        valid1.append(passport)

print(len(valid1)) # 235


# part 2
def byr_isvalid(pp):
    return '1920' <= pp['byr'] <= '2002'

def iyr_isvalid(pp):
    return '2010' <= pp['iyr'] <= '2020'

def eyr_isvalid(pp):
    return '2020' <= pp['eyr'] <= '2030'

def hgt_isvalid(pp):
    if pp['hgt'][-2:] == 'cm':
        return 150 <= int(pp['hgt'][:-2]) <= 193
    if pp['hgt'][-2:] == 'in':
        return 59 <= int(pp['hgt'][:-2]) <= 76
    return False

def hcl_isvalid(pp):
    if pp['hcl'][0] == '#':
        for char in pp['hcl'][1:]:
            if not (('0' <= char <= '9') or ('a' <= char <= 'f')):
                return False
        return True
    return False

def ecl_isvalid(pp):
    return pp['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def pid_isvalid(pp):
    if len(pp['pid']) == 9:
        try:
            int(pp['pid'])
            return True
        except:
            return False
    return False

def pp_isvalid(pp):
    checks = [byr_isvalid, iyr_isvalid, eyr_isvalid, hgt_isvalid, hcl_isvalid, ecl_isvalid, pid_isvalid]
    for check in checks:
        if not check(pp):
            return False
    return True

valid2 = 0
for passport in valid1:
    if pp_isvalid(passport):
        valid2 += 1

print(valid2) # 194