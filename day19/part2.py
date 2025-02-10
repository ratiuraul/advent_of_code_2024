from os import path
from collections import defaultdict
from functools import cache
FILE_PATH = path.realpath("day19/input.txt")

options = defaultdict(int)


@cache  # if the method is called again with the same arg, it will return directly
def valid_design(design: str) -> bool:
    if design == "":
        return 1
    count = 0
    for towel in towels:
        if design.startswith(towel):
            count += valid_design(design[len(towel):])
    return count


with open(FILE_PATH) as f:
    file_content = list(map(str.strip, f.readlines()))
    towels = file_content[0].split(', ')
    designs = file_content[2:]


combinations = [valid_design(design) for design in designs]

print(sum(combinations))
