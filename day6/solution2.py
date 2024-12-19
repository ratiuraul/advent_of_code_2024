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

start_r, start_c = get_start_position()


def check_for_loop():
    r, c = start_r, start_c
    dr, dc = -1, 0
    visited = set()
    while True:
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        if not (0 <= r + dr < max_row and 0 <= c+dc < max_col):
            return False
        if map[r+dr][c+dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc


part2 = 0
for row in range(max_row):
    for col in range(max_col):
        if map[row][col] != '.':
            continue
        map[row][col] = "#"
        if check_for_loop():
            part2 += 1
        map[row][col] = '.'

print(part2)
