from os import path
from collections import defaultdict
rules_path = path.realpath('day5/input_rules.txt')
updates_path = path.realpath('day5/input_updates.txt')

with open(rules_path) as f:
    rules_content = f.readlines()


with open(updates_path) as f:
    updates_content = f.readlines()


invalid_map = defaultdict(bool)
sum = 0

for x, y in [tuple(map(int, l.split("|"))) for l in rules_content]:
    invalid_map[(y, x)] = True


def check_line(line: list[int]) -> bool:
    for i in range(len(line_numbers)):
        for j in range(i+1, len(line_numbers)):
            if invalid_map[(line[i], line[j])]:
                return False

    return True


for line in updates_content:
    line_numbers = [int(num) for num in line.strip().split(',')]
    if check_line(line_numbers):
        sum += line_numbers[len(line_numbers)//2]

print(sum)