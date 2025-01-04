from os import path
from collections import namedtuple

PATH = path.realpath('day9/input.txt')

with open(PATH) as f:
    disk_map = list(map(int, list(f.read())))

is_file = True
files = {}
spaces = []
ptr = 0

for i, size in enumerate(disk_map):
    if is_file:
        files[i//2] = (ptr, size)
    else:
        spaces.append((ptr, size))
    is_file = not is_file
    ptr += size

# 00...111...2...333.44.5555.6666.777.888899
print()

for file in reversed(files):
    file_index, file_size = files[file]
    space_id = 0
    while space_id < len(spaces):
        space_loc, space_size = spaces[space_id]
        if space_loc > file_index:
            break
        if file_size == space_size:
            files[file] = (space_loc, file_size)
            spaces.pop(space_id)
            break
        if file_size < space_size:
            files[file] = (space_loc, file_size)
            spaces[space_id] = (space_loc + file_size, space_size-file_size)
            break
        space_id += 1


checksum = 0
for file_id, (file_loc, file_size) in files.items():
    for i in range(file_loc, file_loc + file_size):
        checksum += i*file_id
print(checksum)
