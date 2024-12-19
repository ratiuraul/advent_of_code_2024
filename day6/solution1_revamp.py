from os import path

file_path = path.realpath("day6/input.txt")

with open(file_path) as f:
    map = list(map(list, map(str.strip, f.readlines())))


def get_start_position():
    for r, row in enumerate(map):
        for c, val in enumerate(row):
            if val == '^':
                return (r, c)


max_row = len(map)
max_col = len(map[0])

r, c = get_start_position()
dr, dc = -1, 0
visited = set()

while True:
    visited.add(r, c)
    if not (0 <= r + dr < max_row and 0 <= c+dc < max_col):
        break
    if map[r+dr][c+dc] == "#":
        dc, dr = -dr, dc
    else:
        r += dr
        c += dc

print(len(visited))
