from os import path
from collections import defaultdict, deque

FILE_PATH = path.realpath('day12/input.txt')

with open(FILE_PATH)as f:
    garden = list(map(str.strip, f.readlines()))

max_row = len(garden)
max_col = len(garden[0])
plant_map = defaultdict(list)


def count_region_perimeter(region):
    total = 0
    same_type_neighbours = 0
    for r, c in region:
        for nr, nc in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            if (r+nr, c+nc) in region:
                # same type of plant
                same_type_neighbours += 1
        total += 4 - same_type_neighbours
    return total


def same_neighbours(plant: tuple) -> int:
    plant_row, plan_col = plant
    same_neighbours = []
    for r, c in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
        nr, nc = (plant_row+r, plan_col+c)
        if 0 <= nr < max_row and 0 <= nc < max_col:
            # neighbour is same plant
            if garden[plant_row][plan_col] == garden[nr][nc]:
                same_neighbours.append((nr, nc))

    return same_neighbours


area = 0
regions = []
seen = set()
for r, row in enumerate(garden):
    for c, plant in enumerate(row):
        if (r, c) in seen:
            continue
        region = set()
        queue = deque([(r, c)])
        while queue:
            rr, cc = queue.popleft()
            region.add((rr, cc))
            seen.add((rr, cc))
            neighbours = same_neighbours((rr, cc))
            for neighbour in neighbours:
                if neighbour not in seen:
                    queue.append(neighbour)
        regions.append(region)

total_price = 0

for region in regions:
    region_perimeter = count_region_perimeter(region)
    area = len(region)
    total_price += area*region_perimeter

print(total_price)
