from os import path

file_path = path.realpath("day6/input.txt")

with open(file_path) as f:
    map = f.readlines()

guard = [">", "<", "^", "v"]
GUARDIAN_LEFT = False
visited_positions = set()


def get_guard_position(current_map):
    for r, row in enumerate(map):
        for c, _ in enumerate(row):
            if current_map[r][c] in guard:
                return (r, c)


def move_guardian(s, new_s, index):

    if index < 0:  # add it to the beginning
        return new_s + s
    if index > len(s):  # add it to the end
        return s + new_s

    # insert the new string between "slices" of the original
    return s[:index] + new_s + s[index + 1:]


def move_up(current_map, r, c):
    global GUARDIAN_LEFT
    guardian = current_map[r][c]
    while guardian != '#':
        visited_positions.add((r, c))
        current_map[r] = move_guardian(current_map[r], '.', c)
        current_map[r-1] = move_guardian(current_map[r-1], '^', c)
        r -= 1
        if r == 0:
            GUARDIAN_LEFT = True
            visited_positions.add((r, c))
            return
        guardian = current_map[r-1][c]

    move_right(current_map, r, c)


def move_right(current_map, r, c):
    global GUARDIAN_LEFT
    guardian = current_map[r][c]
    max_columns = len(current_map[r])-1
    while guardian != '#':
        visited_positions.add((r, c))
        current_map[r] = move_guardian(current_map[r], '.', c)
        current_map[r] = move_guardian(current_map[r], '>', c+1)
        c += 1
        if c == max_columns:
            GUARDIAN_LEFT = True
            visited_positions.add((r, c))
            return
        guardian = current_map[r][c+1]
    move_down(current_map, r, c)


def move_down(current_map, r, c):
    global GUARDIAN_LEFT
    guardian = current_map[r][c]
    max_rows = len(map)-1
    while guardian != '#':
        visited_positions.add((r, c))
        current_map[r] = move_guardian(current_map[r], '.', c)
        current_map[r+1] = move_guardian(current_map[r+1], 'V', c)
        r += 1
        if r == max_rows:
            GUARDIAN_LEFT = True
            visited_positions.add((r, c))
            return
        guardian = current_map[r+1][c]

    move_left(current_map, r, c)


def move_left(current_map, r, c):
    global GUARDIAN_LEFT
    guardian = current_map[r][c]
    while guardian != '#':
        visited_positions.add((r, c))
        current_map[r] = move_guardian(current_map[r], '.', c)
        current_map[r] = move_guardian(current_map[r], '<', c-1)
        if c == 0:
            GUARDIAN_LEFT = True
            visited_positions.add((r, c))
            return
        c -= 1
        guardian = current_map[r][c-1]
    move_up(current_map, r, c)


cr, cc = get_guard_position(map)
if map[cr][cc] == "^":
    move = move_up
elif map[cr][cc] == "v":
    move = move_down
elif map[cr][cc] == "<":
    move = move_left
else:
    move = move_right

while not GUARDIAN_LEFT:
    move(map, cr, cc)

print(len(visited_positions))
