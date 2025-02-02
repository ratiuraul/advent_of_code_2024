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

storage_map = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@."
}


def get_next_pos(current_pos, move):
    cr, cc = current_pos
    if move == ">":
        return (cr, cc + 1)
    if move == "v":
        return (cr + 1, cc)
    if move == "<":
        return (cr, cc-1)
    if move == "^":
        return (cr-1, cc)
    print(f"MOVE: {move}")


scaled_storage = []
for line in storage:
    new_line = ""
    for val in line:
        new_line += storage_map[val]
    scaled_storage.append(new_line)

for ri, r in enumerate(scaled_storage):
    for ci, c in enumerate(r):
        current_pos = (ri, ci)
        current_element = scaled_storage[ri][ci]
        if current_element == "#":
            walls.append(current_pos)
        elif current_element in ["["]:
            next_pos = get_next_pos((ri, ci), ">")
            boxes.append([current_pos, next_pos])
            ri, ci = next_pos
        elif current_element == "@":
            robot_pos = current_pos


def move_side(side_pos, move, boxes):
    while True:
        next_pos = get_next_pos(side_pos, move)
        if next_pos in walls:
            break
        for box in boxes:
            if next_pos in box:
                if side_pos in box:
                    return next_pos
                return move_side(next_pos, move, boxes)
        return next_pos


def move_box(box, move, boxes):
    global box_moved
    left_side, right_side = box
    move_left = move_side(left_side, move, boxes)
    partial_boxes = boxes
    if move_left:
        partial_boxes.remove(box)
        partial_boxes.append([right_side, move_left])
    move_right = move_side(right_side, move, partial_boxes)
    if move_right and move_left:
        box_moved = True
        partial_boxes.remove(box)
        partial_boxes.append([move_right, move_left])
    else:
        # boxes unchanged
        box_moved = False
        partial_boxes = boxes
    return partial_boxes


for move in moves:
    box_moved = False
    next_pos = get_next_pos(robot_pos, move)
    if next_pos in walls:
        continue
    else:
        for box in boxes:
            if next_pos in box:
                boxes = move_box(box, move, boxes)
                if box_moved:
                    robot_pos = next_pos
                    continue
    robot_pos = next_pos

print(sum([100*box[0] + box[1] for box in boxes]))
