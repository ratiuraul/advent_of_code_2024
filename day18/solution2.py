from os import path
from collections import deque

FILE_PATH = path.realpath('day18/input.txt')

with open(FILE_PATH) as f:
    byte_positions = list(map(str.strip, f.readlines()))

max_col = 71
max_row = 71
fallen_bytes = []
for byte_position in byte_positions:
    x, y = byte_position.split(',')
    fallen_bytes.append((int(x),  int(y)))


def count_steps(num_blocks):
    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    while queue:
        r, c, distance = queue.popleft()
        node = (r, c)
        if node in visited:
            continue
        visited.add(node)
        if (r, c) == (max_row, max_col):
            return distance
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nr, nc = r+dr, c+dc
            if not (0 <= nr <= max_row and 0 <= nc <= max_col):
                continue
            if (nr, nc) not in fallen_bytes[:num_blocks]:
                queue.append((nr, nc, distance + 1))
    return -1


print(count_steps(1024))

# We use binary search to split the bytes into halfes and repeat the search


lo, hi = 0, len(fallen_bytes) - 1
while lo < hi:
    mid = (lo + hi) // 2
    if count_steps(mid + 1) != -1:
        # not blocked road , we are at the end, not our searched element
        lo = mid + 1
    else:
        # road is blocked, is there any other lower number?

        hi = mid


part2 = ",".join(str(x) for x in fallen_bytes[lo])
print(f"Part 2: {part2}")
