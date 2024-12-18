if __name__ == '__main__':
    print('Advent of Code 2024 - Day 11')

    with open('day11.txt') as f:
        stones = [int(num) for num in f.read().strip().split()]

    #stones = [125, 17]

    cache = {}
    def stones_len_after_blink(stones: list[int], final_blink: int) -> int:

        def stone_blink(stone: int, blink: int) -> list[int]:
            new_stones = []

            if blink == 1:
                if stone == 0:
                    new_stones = [1]
                elif len(str(stone)) % 2 == 0:
                    mid = len(str(stone)) // 2
                    new_stones = [int(str(stone)[:mid]), int(str(stone)[mid:])]
                else:
                    new_stones = [stone * 2024]

                cache[(stone, blink)] = new_stones
                return new_stones

            for s in stone_blink(stone, blink - 1):
                new_stones += stone_blink(s, 1)

            cache[(stone, blink)] = new_stones
            return new_stones

        total_stones = 0
        for stone in stones:
            total_stones += len(stone_blink(stone, final_blink))

        return total_stones
            
    print(f'Part 1: {stones_len_after_blink(stones, 25)}') # 231278

    print(f'Part 2: {stones_len_after_blink(stones, 75)}') #
