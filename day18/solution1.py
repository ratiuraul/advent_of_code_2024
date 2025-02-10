from os import path
from collections import deque

FILE_PATH = path.realpath('day18/input.txt')

with open(FILE_PATH) as f:
    byte_positions = list(map(str.strip, f.readlines()))
    # byte_positions = list(
    #     map(tuple, (map(lambda x: x.replace(',', ''), (map(str.strip, f.readlines()))))))


max_col = 70
max_row = 70
fallen_bytes = []
for byte_position in byte_positions[0:1024]:
    x, y = byte_position.split(',')
    fallen_bytes.append((int(x),  int(y)))
queue = deque([(0, 0, 0)])
# visited = set((0, 0))
visited = []

while queue:
    r, c, distance = queue.popleft()
    node = (r, c)
    if node in visited:
        continue
    visited.append(node)
    if (r, c) == (max_row, max_col):
        break
    for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nr, nc = r+dr, c+dc
        if not (0 <= nr <= max_row and 0 <= nc <= max_col):
            continue
        if (nr, nc) not in fallen_bytes:
            queue.append((nr, nc, distance + 1))

print(distance)
