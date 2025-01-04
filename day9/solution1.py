from os import path
from collections import namedtuple

PATH = path.realpath('day9/input.txt')
file_id = namedtuple("file_id", ["id", "occurrences"])
free_spaces = namedtuple("free_spaces", ["index", "blocks"])


with open(PATH) as f:
    disk_map = list(map(int, list(f.read())))


disk = []

for i in range(0, len(disk_map), 2):
    disk.extend(disk_map[i]*[i//2])
    if i + 1 < len(disk_map):
        disk.extend(disk_map[i+1]*[-1])

empties = [i for i, val in enumerate(disk) if val == -1]
i = 0
while True:
    while disk[-1] == -1:
        disk.pop()
    target = empties[i]
    if target >= len(disk):
        break
    disk[target] = disk.pop()
    i += 1

checksum = 0
for i, value in enumerate(disk):
    checksum += i*value
print(checksum)
