from os import path

file_path = path.realpath('day25/input.txt')

with open(file_path) as f:
    data = f.read().split('\n\n')

format_data = [line.split('\n') for line in data]

locks = []
keys = []

for el in format_data:
    if el[0][0] == "#":
        locks.append(el)
    else:
        keys.append(el)

lock_heights = []
keys_heights = []


def calculate_height(input):
    height = [0, 0, 0, 0, 0]
    for _, row in enumerate(input):
        for c, col in enumerate(row):
            if col == '#':
                height[c] += 1
    return height


for lock in locks:
    lock_height = calculate_height(lock[1:])
    lock_heights.append(lock_height)

for key in keys:
    key_height = calculate_height(key[5::-1])
    keys_heights.append(key_height)

res = 0

for kh in keys_heights:
    for lh in lock_heights:
        if all([kh[i] + lh[i] <= 5 for i in range(len(kh))]):
            res += 1
print(res)
