from os import path
from collections import deque, defaultdict

FILE_PATH = path.realpath('day20/input.txt')

with open(FILE_PATH) as f:
    grid = list(map(str.strip, f.readlines()))

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if grid[r][c] == 'S':
            start = (r, c)
            break
    else:  # if for reaches end
        continue
    break
target_savings = 100
num_rows = len(grid)
num_cols = len(grid[0])

queue = deque([(r, c, 0)])

dists = {}

while queue:
    r, c, d = queue.popleft()
    if (r, c) in dists:
        continue
    dists[(r, c)] = d
    for nr, nc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
        if grid[nr][nc] != "#":
            queue.appendleft((nr, nc, d+1))

shortcuts = defaultdict(int)
for r in range(num_rows):
    for c in range(num_cols):
        for r2, c2 in [
                (r-2, c),
                (r+2, c),
                (r, c-2),
                (r, c+2),
                (r+1, c+1),
                (r+1, c-1),
                (r-1, c+1),
                (r-1, c-1)]:
            if (r, c) not in dists or (r2, c2) not in dists:
                continue
            time_save = dists[(r2, c2)] - dists[(r, c)] - 2
            if time_save >= target_savings:
                shortcuts[time_save] += 1

print(sum(shortcuts.values()))
