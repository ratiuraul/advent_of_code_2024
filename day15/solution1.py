from os import path

FILE_PATH = path.relpath("day15/input.txt")

with open(FILE_PATH) as f:
    input = f.read().split('\n\n')
    storage = input[0].split('\n')
    moves = input[1].replace('\n', '')

walls = []
boxes = []
robot_pos = None
box_moved = False

for ri, r in enumerate(storage):
    for ci, c in enumerate(r):
        current_pos = (ri, ci)
        current_element = storage[ri][ci]
        if current_element == "#":
            walls.append(current_pos)
        elif current_element == "O":
            boxes.append(current_pos)
        elif current_element == "@":
            robot_pos = current_pos


def move_box(box_pos, move):
    global box_moved
    box_positions = [box_pos]
    while box_positions:
        next_pos = get_next_pos(box_positions.pop(), move)
        if next_pos in walls:
            break
        elif next_pos in boxes:
            box_positions.append(next_pos)
        else:
            boxes.remove(box_pos)
            boxes.append(next_pos)
            box_moved = True


def get_next_pos(current_pos, move):
    cr, cc = current_pos
    if move == ">":
        return (cr, cc + 1)
    if move == "v":
        return (cr+1, cc)
    if move == "<":
        return (cr, cc-1)
    if move == "^":
        return (cr-1, cc)
    print(f"MOVE: {move}")


for move in moves:
    box_moved = False
    next_pos = get_next_pos(robot_pos, move)
    if next_pos in walls:
        continue
    elif next_pos in boxes:
        move_box(next_pos, move)
        if box_moved:
            robot_pos = next_pos
    else:
        robot_pos = next_pos

print(sum([100*box[0] + box[1] for box in boxes]))
