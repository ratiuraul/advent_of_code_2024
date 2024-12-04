from os import path
import re
file_path = path.realpath('day3/input.txt')

REGEX_PATTERN = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"


with open(file_path) as f:
    instructions = f.read()

matches = re.findall(REGEX_PATTERN, instructions)

result = 0
enabled = True
for inst in matches:
    match inst:
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _:
            if enabled:
                x, y = map(int, inst[4:-1].split(','))
                result += x*y

print(result)
