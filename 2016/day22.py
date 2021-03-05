print('Advent of Code - Day 22')
class FileSystem:
    def __init__(self, x, y, used, avail):
        self.x = x
        self.y = y
        self.used = used
        self.avail = avail

    @staticmethod
    def arrange_descending_avail(filesystems):
        return sorted(filesystems, key=lambda x: x.avail, reverse=True)

    @staticmethod
    def arrange_ascending_used(filesystems):
        return sorted(filesystems, key=lambda x: x.used)

with open('day22.txt') as f:
    df = []
    for line in [filesystem for filesystem in f.read().splitlines() 
        if filesystem.startswith('/dev/grid/node')]:
            _, x, y, _, used, avail, _ = line.replace('-', ' ').split()
            x, y = int(x.lstrip('x')), int(y.lstrip('y'))
            used, avail = int(used.rstrip('T')), int(avail.rstrip('T'))
            df.append(FileSystem(x, y, used, avail))


# part 1
descending_avail = FileSystem.arrange_descending_avail(df)
ascending_used = FileSystem.arrange_ascending_used(df) 
viable_pairs = 0

for source in ascending_used:
    if source.used == 0:
        continue

    for destination in descending_avail:
        if source == destination:
            continue
        
        if source.used <= destination.avail:
            viable_pairs += 1
        else:
            break


print(f'Part 1: {viable_pairs}') # 872

