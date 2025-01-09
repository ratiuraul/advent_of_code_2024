from os import path
import re

FILE_PATH = path.realpath('day13/input.txt')

A_REGEX_PATTERN = "(Button A:).*X\+(\d*).*Y\+(\d*)"
B_REGEX_PATTERN = "(Button B:).*X\+(\d*).*Y\+(\d*)"
PRIZE_REGEX_PATTERN = "(Prize:).*X=(\d*),.*Y=(\d*)"
PRICE_A = 3
PRICE_B = 1

with open(FILE_PATH) as f:
    content = f.read().split('\n\n')


def find_cost(machine):
    # we use Cramer's law for linear ecuations
    a1, a2 = machine["A"]
    b1, b2 = machine["B"]
    c1, c2 = machine["PRIZE"]

    det_m = (a1*b2) - (a2*b1)
    det_x = ((10000000000000+c1)*b2) - ((10000000000000+c2)*b1)
    det_y = (a1*(10000000000000+c2)) - (a2*(10000000000000+c1))

    if det_m != 0:
        x = det_x / det_m
        y = det_y / det_m

        if int(x) == x and int(y) == y:
            return PRICE_A*x + PRICE_B*y
    return 0


machines = []

for entry in content:
    a = re.search(A_REGEX_PATTERN, entry)
    b = re.search(B_REGEX_PATTERN, entry)
    prize = re.search(PRIZE_REGEX_PATTERN, entry)
    machines.append({
        "A": (int(a.group(2)), int(a.group(3))),
        "B": (int(b.group(2)), int(b.group(3))),
        "PRIZE": (int(prize.group(2)), int(prize.group(3)))
    })

total_cost = 0
for machine in machines:
    total_cost += find_cost(machine)
print(total_cost)
