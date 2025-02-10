from os import path
FILE_PATH = path.realpath("day19/input.txt")


def valid_design(design: str) -> bool:
    if design in towels:
        return True
    for towel in towels:
        if design.startswith(towel):
            if valid_design(design[len(towel):]):
                return True
    return False


with open(FILE_PATH) as f:
    file_content = list(map(str.strip, f.readlines()))
    towels = file_content[0].split(', ')
    designs = file_content[2:]


valid_designs = len([design for design in designs if valid_design(design)])
print(valid_designs)
