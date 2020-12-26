with open('day03.txt') as f:
    given = [line.replace('#','').replace('@ ','').replace(
        ':','').split(' ') for line in f.read().splitlines()]
    claims = []
    for claim in given:
        temp = []
        temp.append(int(claim[0]))
        x, y = claim[1].split(',')
        temp.append([int(x), int(y)])
        w, h = claim[2].split('x')
        temp.append([int(w), int(h)])
        claims.append(temp)

# part 1
cloth = [[0]*1000 for _ in range(1000)]
overlap = set()
for claim in claims:
    left, top = claim[1]
    width, height = claim[2]
    for y in range(top, top + height):
        for x in range(left, left + width):
            if cloth[y][x] >= 1:
                overlap.add((y,x))
            cloth[y][x] += 1

print(f'Part 1: {len(overlap)}') # 115242


# part 2
id_claim = None
for claim in claims:
    left, top = claim[1]
    width, height = claim[2]
    for y in range(top, top + height):
        for x in range(left, left + width):
            if cloth[y][x] > 1:
                break
        else:
            continue
        break
    else:
        id_claim = claim[0]
        break
    continue

print(f'Part 2: {id_claim}') # 1046