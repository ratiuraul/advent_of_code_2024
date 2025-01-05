from os import path
from typing import List

FILE_PATH = path.realpath('day11/input.txt')

with open(FILE_PATH) as f:
    arrangement = list(map(int, f.read().strip().split()))


def process_arrangement(arrangement: List):
    pos = 0
    new_arrangement = []
    while True:
        if pos == len(arrangement):
            break
        if arrangement[pos] == 0:
            new_arrangement.append(1)
        elif len(str(arrangement[pos])) % 2 == 0:
            str_num = str(arrangement[pos])
            first_half = int(str_num[:int(len(str_num)/2)])
            secound_half = int(str_num[int(len(str_num)/2):])
            new_arrangement.append(first_half)
            new_arrangement.append(secound_half)
        else:
            new_arrangement.append(arrangement[pos]*2024)

        pos += 1
    return new_arrangement


def arrangement_after_blink(arrangement: List, blinks: int) -> List:
    new_arrangement = arrangement
    while blinks:
        new_arrangement = process_arrangement(new_arrangement)
        blinks -= 1
    return new_arrangement


sol1 = arrangement_after_blink(arrangement, 75)
print(len(sol1))
