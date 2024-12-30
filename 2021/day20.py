if __name__ == '__main__':
    print("Advent of Code 2021 - Day 20: Trench Map")

    with open('day20.txt') as f:
        algo, raw_image = f.read().strip().split('\n\n')
        light_pixels = set()
        for y, line in enumerate(raw_image.splitlines()):
            for x, char in enumerate(line):
                if char == '#':
                    light_pixels.add((y, x))


    def adj_9(y: int, x: int) -> list[tuple[int, int]]:
        neighbors = []
        for ny in range(y - 1, y + 2):
            for nx in range(x - 1, x + 2):
                neighbors.append((ny, nx))
        return neighbors


    def enhance_image(
        iteration: int,
        minority_pixels: set[tuple[int, int]],
        algo: str
    ) -> set[tuple[int, int]]:
        '''minority_pixels are light pixels if the iteration is odd,
        else they are dark pixels
        '''

        pixel_list = list(minority_pixels)
        y_sorted = sorted(pixel_list)
        min_y, max_y = y_sorted[0][0], y_sorted[-1][0]
        x_sorted = sorted(pixel_list, key=lambda element: element[1])
        min_x, max_x = x_sorted[0][1], x_sorted[-1][1]
        is_alternating = algo[0] == '#' and algo[-1] == '.'

        next_minority_pixels = set()
        pix_str = ''
        for y in range(min_y - 2, max_y + 3):
            for x in range(min_x - 2, max_x + 3):
                pix_str = ''
                for ny, nx in adj_9(y, x):

                    if iteration % 2 == 0 and is_alternating:
                        if (ny, nx) in minority_pixels:
                            pix_str += '0'
                        else:
                            pix_str += '1'

                    else:
                        if (ny, nx) in minority_pixels:
                            pix_str += '1'
                        else:
                            pix_str += '0'

                pix_binary = int(pix_str, 2)
                if iteration % 2 == 1 and is_alternating:
                    if algo[pix_binary] == '.':
                        next_minority_pixels.add((y, x))
                else:
                    if algo[pix_binary] == '#':
                        next_minority_pixels.add((y, x))

        return next_minority_pixels


    def count_pix(repeat: int, pixels: set[tuple[int, int]], algo: str) -> int:
        for i in range(1, repeat + 1):
            pixels = enhance_image(i, pixels, algo)
        return len(pixels)


    print(f'Part 1: {count_pix(2, light_pixels, algo)}') # 5786

    print(f'Part 2: {count_pix(50, light_pixels, algo)}') # 16757

