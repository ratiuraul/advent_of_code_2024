from os import path
file_path = path.realpath('day2/input.txt')


with open(file_path) as f:
    reports = f.readlines()


def is_ascending(a):
    for i in range(len(a) - 1):
        if not (a[i] < a[i+1] and abs(a[i+1] - a[i]) <= 3):
            return i, False
    return 0, True


def is_ascending_safe(a):
    i, result = is_ascending(a)
    if result:
        return True
    else:
        _, result2 = is_ascending(a[0:i]+a[i+1:len(a)])
        _, result3 = is_ascending(a[0:i+1]+a[i+2:len(a)])
        return result2 or result3


def is_descending(a):
    for i in range(len(a) - 1):
        if not (a[i] > a[i+1] and abs(a[i+1] - a[i]) <= 3):
            return i, False
    return 0, True


def is_descending_safe(a):
    i, result = is_descending(a)
    if result:
        return True
    else:
        _, result2 = is_descending(a[0:i]+a[i+1:len(a)])
        _, result3 = is_descending(a[0:i+1]+a[i+2:len(a)])
        return result2 or result3


safe_reports = 0

for report_levels in reports:
    if is_ascending_safe([int(level) for level in report_levels.split()]) or  \
            is_descending_safe([int(level) for level in report_levels.split()]):
        safe_reports += 1


print(safe_reports)
