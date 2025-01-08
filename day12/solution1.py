from os import path
from collections import defaultdict, deque

FILE_PATH = path.realpath('day12/input.txt')

with open(FILE_PATH)as f:
    grid = list(map(str.strip, f.readlines()))

num_rows = len(grid)
num_cols = len(grid[0])


def perimeter(region):
    total = 0
    for r, c in region:
        plant_perimeter = 4
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (r + dr, c+dc) in region:
                plant_perimeter -= 1
        total += plant_perimeter
    return total


regions = []
seen = set()
for r in range(num_rows):
    for c in range(num_cols):
        if (r, c) in seen:
            continue
        region = set()
        queue = deque([(r, c)])
        while queue:
            rr, cc = queue.popleft()
            region.add((rr, cc))
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = rr + dr, cc + dc
                if (
                    (nr, nc) not in seen
                    and 0 <= nr < num_rows
                    and 0 <= nc < num_cols
                    and grid[nr][nc] == grid[rr][cc]
                ):
                    queue.append((nr, nc))
                    seen.add((nr, nc))
        regions.append(region)

print(sum(len(r) * perimeter(r) for r in regions))
