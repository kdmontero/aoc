if __name__ == '__main__':
    print("Advent of Code 2024 - Day 07: Bridge Repair")

    with open('day07.txt') as f:
        equations: list[tuple[int, list[int]]]  = []
        for line in f.read().strip().splitlines():
            raw_value, raw_nums = line.split(': ')
            value = int(raw_value)
            nums = [int(num) for num in raw_nums.split()]
            nums.reverse()
            equations.append((value, nums))


    # part 1

    def can_evaluate1(target: int, current: int, nums: list[int]) -> bool:
        if nums == []:
            return target == current

        if current > target:
            return False

        num = nums.pop()
        if can_evaluate1(target, current + num, nums[:]):
            return True
        if can_evaluate1(target, current * num, nums[:]):
            return True

        return False

    total_calibration1 = 0
    failed_to_eval = []
    for val, nums in equations:
        nums_copy = nums[:]
        current = nums.pop()
        if can_evaluate1(val, current, nums):
            total_calibration1 += val
        else:
            failed_to_eval.append((val, nums_copy))

    print(f'Part 1: {total_calibration1}') # 7579994664753


    # part 2

    def can_evaluate2(target: int, current: int, nums: list[int]) -> bool:
        if nums == []:
            return target == current

        if current > target:
            return False

        num = nums.pop()
        if can_evaluate2(target, current + num, nums[:]):
            return True
        if can_evaluate2(target, current * num, nums[:]):
            return True
        if can_evaluate2(target, int(str(current) + str(num)), nums[:]):
            return True

        return False

    total_calibration2 = total_calibration1
    for val, nums in failed_to_eval:
        current = nums.pop()
        if can_evaluate2(val, current, nums):
            total_calibration2 += val

    print(f'Part 2: {total_calibration2}') # 438027111276610

