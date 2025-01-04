from os import path
from collections import defaultdict
from itertools import combinations

input_file = path.realpath('day8/input.txt')
total_antinodes = set()

with open(input_file) as f:
    input = [line.strip() for line in f.readlines()]

antenas = defaultdict(list)
max_row = len(input)
max_col = len(input[0])


for r, row in enumerate(input):
    for c, col in enumerate(row):
        if col not in ['.', '#']:
            antenas[col].append((r, c))


def get_antinodes(antena):
    antinodes = []
    for pos1, pos2 in combinations(antena, 2):
        r_diff = abs(pos1[0] - pos2[0])
        c_diff = abs(pos1[1] - pos2[1])
        new_r1 = 0
        new_c1 = 0
        new_r2 = 0
        new_c2 = 0
        original_pos1 = pos1
        original_pos2 = pos2
        # uprow
        while True:
            if pos1[1] <= pos2[1]:
                new_c1 = pos1[1] - c_diff
            else:
                new_c1 = pos1[1] + c_diff
            new_r1 = pos1[0] - r_diff
            if 0 <= new_r1 < max_row and 0 <= new_c1 < max_col:
                antinodes.append((new_r1, new_c1))
                pos2 = pos1
                pos1 = (new_r1, new_c1)
            else:
                break

        # back to original position
        pos1 = original_pos1
        pos2 = original_pos2

        # downrow
        while True:
            if pos1[1] <= pos2[1]:
                new_c2 = pos2[1] + c_diff
            else:
                new_c2 = pos2[1] - c_diff
            new_r2 = pos2[0] + r_diff
            if 0 <= new_r2 < max_row and 0 <= new_c2 < max_col:
                antinodes.append((new_r2, new_c2))
                pos1 = pos2
                pos2 = (new_r2, new_c2)
            else:
                break

    return antinodes


for antena in antenas:
    total_antinodes.update(antenas[antena])
    total_antinodes.update(get_antinodes(antenas[antena]))

print(len(total_antinodes))
