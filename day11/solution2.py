from os import path
from functools import cache

FILE_PATH = path.realpath('day11/input.txt')

with open(FILE_PATH) as f:
    arrangement = list(map(int, f.read().strip().split()))

# we count the stones
# each stone is processed individually for a num of blinks
# no need to keep track of entire list since order does not matter
# cache to skip execution for calls with same arguments.


@cache
def count_stones(val: int, blinks: int) -> int:
    if blinks == 0:
        return 1  # no more blinks, one stone is returned
    if val == 0:
        return count_stones(1, blinks - 1)  # zero was processed
    str_val = str(val)
    len_str_val = len(str_val)
    if len_str_val % 2 == 0:
        # two stones needs to be processed(left +right digits)
        first_half = int(str_val[:int(len_str_val/2)])
        secound_half = int(str_val[int(len_str_val/2):])
        return count_stones(first_half, blinks - 1) + count_stones(secound_half, blinks - 1)
    return count_stones(val*2024, blinks-1)


# for each stone, count how many stone will it generate after a num of blinks
part2 = sum(count_stones(s, 75) for s in arrangement)

print(part2)
