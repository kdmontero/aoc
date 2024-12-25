import re

class Workflow:
    def __init__(self, name: str, rules: list[str]) -> None:
        self.name = name
        self.default = rules[-1]
        self.rules = []
        rule_pattern = re.compile(r'(([xmas])[<>][0-9]+):([ARa-z]+)')
        for rule in rules[:-1]:
            condition, rating, result = rule_pattern.findall(rule)[0]
            self.rules.append((rating, condition, result))
        
    
    @staticmethod
    def check(
        rule: tuple[str, str, str], 
        part: dict[str, int]
    ) -> bool | str:
        rating, condition, result = rule
        if eval(condition.replace(rating, str(part[rating]))):
            return result
        return False

    def check_rules(self, part: dict[str, int]) -> str:
        for rule in self.rules:
            result = self.check(rule, part)
            if result:
                return result
        return self.default

if __name__ == '__main__':
    print("Advent of Code 2023 - Day 19: Aplenty")

    with open('day19.txt') as f:
        raw_workflow, raw_parts = f.read().split('\n\n')
        workflow = {}
        wf_pattern = re.compile(r'([a-z]+)\{(.+)\}')
        for line in raw_workflow.splitlines():
            name, rules = wf_pattern.findall(line)[0]
            workflow[name] = Workflow(name, rules.split(','))

        parts = []
        for line in raw_parts.splitlines():
            part = eval(line
                .replace('x', '"x"')
                .replace('m', '"m"')
                .replace('a', '"a"')
                .replace('s', '"s"')
                .replace('=', ':')
            )
            parts.append(part)


    # part 1
    def check_workflows(part: dict[str, int]) -> bool:
        wf = 'in'
        while wf not in {'A', 'R'}:
            wf = workflow[wf].check_rules(part)
        if wf == 'A':
            return True
        elif wf == 'R':
            return False
    
    accepted_parts = []
    for part in parts:
        if check_workflows(part):
            accepted_parts.append(part)
    
    rating_total = 0
    for part in accepted_parts:
        rating_total += sum(part.values())

    print(f'Part 1: {rating_total}') # 325952


    print(f'Part 2: {0} - Not Implemented') #