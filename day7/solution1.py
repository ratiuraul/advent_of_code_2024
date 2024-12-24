from os import path
import operator
import itertools

file_path = path.realpath('day7/input.txt')

with open(file_path) as f:
    lines = f.readlines()

calibrations = 0


def check_calibraion(test_value, operands):

    if len(operands) == 1:
        return test_value == operands[0]

    if test_value % operands[-1] == 0:
        if check_calibraion(
            test_value / operands[-1],
            operands[:-1]
        ):
            return True
    if test_value - operands[-1] >= 0:
        if check_calibraion(
            test_value - operands[-1],
            operands[:-1]
        ):
            return True
    return False


for line in lines:
    test_value = int(line.split(":")[0])
    operands = list(map(int, line.strip().split(":")[1].split()))
    if check_calibraion(test_value, operands):
        calibrations += test_value

print(calibrations)
