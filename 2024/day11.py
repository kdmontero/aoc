from functools import lru_cache


if __name__ == '__main__':
    print('Advent of Code 2024 - Day 11')

    with open('day11.txt') as f:
        stones = [int(num) for num in f.read().strip().split()]

    @lru_cache(maxsize=None)
    def stone_blink(stone: int, blink: int) -> int:
        if blink == 0:
            return 1

        if stone == 0:
            return stone_blink(1, blink - 1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            right_stone = stone_blink(int(str(stone)[:mid]), blink - 1)
            left_stone = stone_blink(int(str(stone)[mid:]), blink - 1)
            return right_stone + left_stone
        else:
            return stone_blink(stone * 2024, blink - 1)

    def stones_len_after_blink(stones: list[int], final_blink: int) -> int:
        total_stones = 0
        for stone in stones:
            total_stones += stone_blink(stone, final_blink)

        return total_stones
            
    print(f'Part 1: {stones_len_after_blink(stones, 25)}') # 231278

    print(f'Part 2: {stones_len_after_blink(stones, 75)}') # 274229228071551

