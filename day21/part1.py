# metoda recursiva prin care sa generam secventa de la fiecare robot
# i.e ca sa apas A pe primu, ce trb sa apas pe al 3lea
# BFS sa gasim drumu cel mai scurt pe numeric keypad
# dupa ce avem drumu cel mai scurt, apelam metoda recusiva


from os import path
from collections import deque
import re

FILE_PATH = path.realpath('day21/input.txt')
NUM_RE = '[1-9][0-9]*'

with open(FILE_PATH) as f:
    sequences = map(str.strip, f.readlines())

numeric_keypad = {
    (0, 0): '7',
    (0, 1): '8',
    (0, 2): '9',
    (1, 0): '4',
    (1, 1): '5',
    (1, 2): '6',
    (2, 0): '1',
    (2, 1): '2',
    (2, 2): '3',
    # (3, 0): 'PANIC',
    (3, 1): '0',
    (3, 2): 'A',
}

directional_keypad = {
    # (0, 0): 'PANIC',
    (0, 1): '^',
    (0, 2): 'A',
    (1, 0): '<',
    (1, 1): 'v',
    (1, 2): '>',
}


directions = {
    (1, 0):  'v',
    (0, -1): '<',
    (0, 1):  '>',
    (-1, 0): '^'
}

sequence = '<A^A>^^AvvvA'


def generate_pad_sequence(sequence, initial_pos, pad) -> str:
    complete_trace = ''
    current_pos = initial_pos
    for button in sequence:
        cr, cc = current_pos
        visited = []
        queue = deque([(cr, cc, '')])
        while queue:
            r, c, trace = queue.popleft()
            if pad[(r, c)] == button:
                current_pos = (r, c)
                break
            if (r, c) in visited:
                continue
            visited.append((r, c))
            for dr, dc in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in pad.keys():
                    queue.append((nr, nc, trace+directions[(dr, dc)]))
        complete_trace += trace + 'A'
    return complete_trace


# v<A<AA>>^AvA<^A>Av<A<A>>^AvAA<^A>Av<<A>>^AAvA^Av<A>^AA<A>Av<A<A>>^AAAvA<^A>A'
# v<<A>^Av<A>>^A<AA>AvAA^Av<AAA>^A
# <^<A^^A>>AvvvA
# 179A
result = 0
for seq in sequences:
    new_sequence = generate_pad_sequence(seq, (3, 2), numeric_keypad)
    seq_val = int(re.search(NUM_RE, seq).group())
    for _ in range(2):
        new_sequence = generate_pad_sequence(
            new_sequence, (0, 2), directional_keypad)
    result += seq_val*len(new_sequence)
print(result)
