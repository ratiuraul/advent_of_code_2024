from os import path
file_path = path.realpath('day2/input.txt')


with open(file_path) as f:
    reports = f.readlines()


def is_safe_report(a):
    if all([a[i] < a[i+1] and abs(a[i+1] - a[i]) <= 3 for i in range(len(a) - 1)]) \
            or all([a[i] > a[i+1] and abs(a[i+1] - a[i]) <= 3 for i in range(len(a) - 1)]):
        return True
    return False


safe_reports = 0
for report_levels in reports:
    if is_safe_report([int(level) for level in report_levels.split()]):
        safe_reports += 1

print(safe_reports)
