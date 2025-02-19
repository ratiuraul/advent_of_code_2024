from os import path
from collections import OrderedDict
FILE_PATH = path.realpath('day24/input.txt')

with open(FILE_PATH) as f:
    file_content = f.read()
    gates = file_content.split('\n\n')[0].split('\n')
    ops = file_content.split('\n\n')[1].split('\n')

gates_dict = {}
ops_dict = {}

operators = {
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'XOR': lambda x, y: x ^ y
}

for gate in gates:
    gates_dict[gate.split(':')[0]] = gate.split(':')[1].strip()

for op in ops:
    ls = op.split('->')[0]
    dest = op.split('->')[1].strip()
    for operator in operators:
        if operator not in ls:
            continue
        ops_dict[dest] = {
            'operands': list(map(str.strip, ls.split(operator))),
            'operator': operator
        }

z_gates = OrderedDict()
bits = []
for key in sorted(ops_dict.keys()):
    if key.startswith('z'):
        z_gates[key] = ops_dict[key]

# update the gates dict  for all the gates
gates_not_updated = [gate for gate in ops_dict if gate not in gates_dict]

while gates_not_updated:
    gate = gates_not_updated
    for gate, op in ops_dict.items():
        if all([operand in gates_dict.values() for operand in op["operands"]]):
            op1 = op['operands'][0]
            op2 = op['operands'][1]
            operation = op['operator']
            gates_dict[gate] = operators[operation](
                int(gates_dict[op1]), int(gates_dict[op2]))
        else:


for key_dict in z_gates.values():
    # operand value might not yet be caculated
    op1 = key_dict['operands'][0]
    op2 = key_dict['operands'][1]
    operation = key_dict['operator']
    output = operators[operation](int(gates_dict[op1]), int(gates_dict[op2]))
    bits.insert(0, output)

result = 0
for i, bit in enumerate(bits[::-1]):
    result += 2 ^ i * bit

print(result)
