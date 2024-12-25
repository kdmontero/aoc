if __name__ == '__main__':
    print("Advent of Code 2021 - Day 10: Syntax Scoring")

    with open('day10.txt') as f:
        lines = f.read().splitlines()

    close = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
        }

    corrupted_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
        }


    # part 1

    def is_corrupted(line):
        stack = []
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif char == close.get(stack[-1]):
                stack.pop()
            else:
                return corrupted_score[char]
        return False

    incomplete_lines = []
    syntax_error_score = 0
    for line in lines:
        score = is_corrupted(line)
        if score:
            syntax_error_score += score
        else:
            incomplete_lines.append(line)

    print(f'Part 1: {syntax_error_score}') # 215229
    

    # part 2

    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
        }

    def autocomplete_score(string):
        score = 0
        for char in string:
            score = 5 * score + points[char]
        return score
    
    def autocomplete(line):
        stack = []
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif char == close.get(stack[-1]):
                stack.pop()
        
        end_string = ''
        while stack:
            end_string += close[stack.pop()]

        return end_string
        
    incomplete_scores = []
    for line in incomplete_lines:
        end_string = autocomplete(line)
        incomplete_scores.append(autocomplete_score(end_string))

    middle_score = sorted(incomplete_scores)[len(incomplete_scores)//2]

    print(f'Part 2: {middle_score}') # 1105996483
