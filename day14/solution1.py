from os import path
from math import prod
FILE_PATH = path.realpath("day14/input.txt")
max_col = 100  # 103
max_row = 102  # 101
SECONDS = 100


def get_robot_position(row, column, right, up):
    for _ in range(SECONDS):
        nr = row + up
        nc = column + right
        if nr < 0:
            dif = up + row
            nr = max_row + dif + 1
        elif nr > max_row:
            dif = max_row - row
            nr = up - dif - 1
        if nc > max_col:
            dif = max_col - column
            nc = right - dif - 1
        elif nc < 0:
            dif = right + column
            nc = max_col + dif + 1
        row = nr
        column = nc

    return (nr, nc)


def get_safety_factor(robot_positions):
    q = [0]*4

    mid_c, mid_r = max_col // 2, max_row // 2
    for r, c in robot_positions:
        if r < mid_r:
            if c < mid_c:
                q[0] += 1
            if c > mid_c:
                q[1] += 1
        elif r > mid_r:
            if c < mid_c:
                q[2] += 1
            if c > mid_c:
                q[3] += 1
    return prod(q)


with open(FILE_PATH) as f:
    my_input = list((map(str.strip, f.readlines())))
    grid = []
    for line in my_input:
        pos, vel = tuple(line.split(' '))
        pos = pos.split('=')[1]
        pos = (int(pos.split(',')[0]), int(pos.split(',')[1]))
        vel = vel.split('=')[1]
        vel = (int(vel.split(',')[0]), int(vel.split(',')[1]))
        grid.append((pos, vel))

robot_positions = []
for robot in grid:
    position, move = robot
    column, row = position
    right, up = move
    robot_position = get_robot_position(row, column, right, up)
    robot_positions.append(robot_position)
    print()
safety_factor = get_safety_factor(robot_positions)
print(safety_factor)
