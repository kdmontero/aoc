if __name__ == '__main__':
    print("Advent of Code 2025 - Day 06: Trash Compactor")

    with open('day06.txt') as f:
        worksheet = f.read().strip().splitlines()
    

    # part 1

    numbers_row = worksheet[:-1]
    operations = worksheet[-1].split()
    numbers = []
    for line in numbers_row:
        numbers.append([int(num) for num in line.split()])
        
    def calculate(*numbers: list[int], operation: str) -> int:
        if operation == "+":
            return sum(numbers)
        elif operation == "*":
            answer = 1
            for number in numbers:
                answer *= number
            return answer

    total1 = 0
    for *digits, operation in zip(*numbers, operations):
        total1 += calculate(*digits, operation=operation)

    print(f'Part 1: {total1}') # 3968933219902


    # part 2

    max_line_len = max(len(line) for line in worksheet) + 1
    for i in range(len(worksheet)):
        worksheet[i] = worksheet[i].ljust(max_line_len, ' ')

    total2 = 0
    temp_answer = None
    current_operation = None
    for i in range(max_line_len):
        column = ''.join(line[i] for line in worksheet)

        if column.endswith('+'):
            temp_answer = int(column[:-1])
            current_operation = '+'
        elif column.endswith('*'):
            temp_answer = int(column[:-1])
            current_operation = '*'
        elif column.strip() == '':
            total2 += temp_answer
        else:
            if current_operation == '+':
                temp_answer += int(column)
            elif current_operation == '*':
                temp_answer *= int(column)
    
    print(f'Part 2: {total2}') # 6019576291014

