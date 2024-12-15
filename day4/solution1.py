from os import path
import re
from collections import defaultdict


file_path = path.realpath('day4/input.txt')


with open(file_path) as f:
    lines = f.readlines()

char_map = defaultdict(list)
word_count = 0

for r, row in enumerate(lines):
    for c, val in enumerate(row):
        char_map[val].append((r, c))

for r, c in char_map["X"]:
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        for i, char in enumerate("XMAS"):
            if (r + (dr*i), c+(dc*i)) not in char_map[char]:
                break
        else:
            word_count += 1

print(word_count)
