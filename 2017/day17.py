if __name__ == '__main__':
    print("Advent of Code 2017 - Day 17: Spinlock")

    INPUT = 355

    def spinlock_move(spinlock, step, pos, next_val):
        l = len(spinlock)
        next_pos = ((pos + step + 1) % l)
        spinlock.insert(next_pos, next_val)
        return spinlock, next_pos

    # part 1

    def solve_spinlock_2017(loop, step):
        spinlock = [0]
        next_pos = 0
        for i in range(loop):
            spinlock, next_pos = spinlock_move(spinlock, step, next_pos, i + 1)

        return spinlock[spinlock.index(2017) + 1]

    print(f'Part 1: {solve_spinlock_2017(2017, INPUT)}') # 1912


    # part 2

    def solve_spinlock_0(loop, step):
        zero_pos = 0        # index position of 0
        val = None          # value after the 0
        length = 1          # length of the buffer
        pos = 0             # current position where the value will be inserted

        for i in range(loop):
            pos = ((pos + step + 1) % length)
            length += 1

            # if the current position falls before the index of zero,
            # then the index of zero will increase by 1
            if pos < zero_pos:
                find_val_pos += 1
            
            # if the current position falls in the index of zero, the next
            # value will be the value we are looking for
            elif pos == zero_pos:
                val = i + 1
            
        return val

    print(f'Part 2: {solve_spinlock_0(50_000_000, INPUT)}') # 21066990
