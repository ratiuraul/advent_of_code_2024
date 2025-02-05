from os import path
import re

FILE_PATH = path.realpath('day17/input.txt')

with open(FILE_PATH) as f:
    content = f.read()

a, b, c, *program = list(map(int, re.findall('\d+', content)))

ip = 0
out = []


def combo(operand):
    assert operand != 7, "Invalid operand value"
    if operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c


while ip < len(program):
    opcode = program[ip]
    operand = program[ip+1]
    match opcode:
        case 0:  # adv
            a = a >> combo(operand)
        case 1:  # bxl
            b = b ^ operand
        case 2:  # bst
            b = combo(operand) % 8
        case 3:  # jnz
            if a != 0:
                ip = operand
                continue
        case 4:  # bxc
            b = b ^ c
        case 5:  # out
            out.append(combo(operand) % 8)
        case 6:  # bdv
            b = a >> combo(operand)
        case 7:  # cdv
            c = a >> combo(operand)

    ip += 2

part1 = ','.join(map(str, out))
print(part1)
