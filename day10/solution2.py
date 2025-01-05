from os import path
from collections import deque
# can use list instead of deque but is much slower

INPUT_FILE = path.realpath('day10/input.txt')

with open(INPUT_FILE) as f:
    map = [list(map(int, line.strip())) for line in f.readlines()]

max_row = len(map)
max_col = len(map[0])


def get_rating(row, col):
    endings = []
    queue = deque([(row, col)])

    while queue:
        r, c = queue.popleft()
        if map[r][c] == 9:
            endings.append((r, c))
            continue
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < max_row and 0 <= nc < max_col:
                # we never add the parent node in que due to following condition
                # in this way, all the paths to a 9 are unique
                if map[r][c] + 1 == map[nr][nc]:
                    queue.append((nr, nc))
    return len(endings)


sum = 0
for r, row in enumerate(map):
    for c, _ in enumerate(row):
        if map[r][c] == 0:
            trailhead_score = get_rating(r, c)
            sum += trailhead_score
print(sum)
