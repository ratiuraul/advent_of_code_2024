import sys
import heapq
from os import path

file_path = path.realpath('day16/input.txt')

with open(file_path) as f:
    grid = list(map(str.strip, f.readlines()))


for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == "S":
            start = (r, c)
            break
    else:
        # executed when loop is finished(not break)
        continue
    break

# cost, unde sunte, facing, i.e (0,1) -> Est
# state = cost, r, c, dr, dc
queue = [(0, *start, 0, 1, [start])]
seen = {(*start, 0, 1)}
part1 = 0
best_cost = float("inf")
points = set()

while queue:
    # proprity que, pop always gives the lowest cost
    cost, r, c, dr, dc, path = heapq.heappop(queue)
    seen.add((r, c, dr, dc))  # in seen only lower cost
    if grid[r][c] == "E":
        if cost <= best_cost:
            best_cost = cost
            for point in path:
                points.add(point)
        else:
            break
    # Can we step forward (East in our case) ? Is it in seen?
    if grid[r + dr][c+dc] != "#" and (r+dr, c+dc, dr, dc) not in seen:
        heapq.heappush(queue, (cost + 1, r + dr, c+dc,
                       dr, dc, path + [(r+dr, c+dc)]))
    # after checking if we can go forward, we add all other options
    # check both turns (up, down)
    for ndr, ndc in [(-dc, dr), (dc, -dr)]:
        if (r, c, ndr, ndc) not in seen and grid[r + ndr][c + ndc] != "#":
            heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc, list(path)))


print(len(points))
