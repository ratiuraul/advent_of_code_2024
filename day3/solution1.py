from os import path
import re
file_path = path.realpath('day3/input.txt')

REGEX_PATTERN = 'mul\((\d{1,3}),(\d{1,3})\)'

with open(file_path) as f:
    instructions = f.read()

matches = re.findall(REGEX_PATTERN, instructions)

result = 0
for match in matches:
    multiply = int(match[0]) * int(match[1])
    result += multiply

print(result)
