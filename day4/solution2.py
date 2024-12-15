from os import path
import re
from collections import defaultdict


file_path = path.realpath('day4/input.txt')


with open(file_path) as f:
    lines = f.readlines()

char_map = defaultdict(list)
word_count = 0


def upleft(r, c): return (r - 1, c - 1)


def upright(r, c): return (r - 1, c + 1)


def downleft(r, c): return (r + 1, c - 1)


def downright(r, c): return (r + 1, c + 1)


for r, row in enumerate(lines):
    for c, val in enumerate(row):
        char_map[val].append((r, c))

for r, c in char_map["A"]:
    if upleft(r, c) in char_map["M"]:
        if (
            downleft(r, c) in char_map["M"]
            and upright(r, c) in char_map["S"]
            and downright(r, c) in char_map["S"]
        ):
            word_count += 1
        elif (
            upright(r, c) in char_map["M"]
            and downleft(r, c) in char_map["S"]
            and downright(r, c) in char_map["S"]
        ):
            word_count += 1
    elif downright(r, c) in char_map["M"]:
        if (
            downleft(r, c) in char_map["M"]
            and upright(r, c) in char_map["S"]
            and upleft(r, c) in char_map["S"]
        ):
            word_count += 1
        elif (
            upright(r, c) in char_map["M"]
            and downleft(r, c) in char_map["S"]
            and upleft(r, c) in char_map["S"]
        ):
            word_count += 1


print(word_count)
