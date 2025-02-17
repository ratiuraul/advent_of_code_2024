from os import path
from collections import defaultdict
FILE_PATH = path.realpath('day22/input.txt')

with open(FILE_PATH) as f:
    numbers = list(map(int, f.readlines()))


def mix(num: int, secret_num: int) -> int:
    return num ^ secret_num


def prune(secret_num: int) -> int:
    return secret_num % 16777216


sequences = defaultdict(list)


def get_sequences(prices):
    start = 0
    entire_sequence = [prices[j+1] - prices[j] for j in range(len(prices)-1)]
    for i in range(4, len(prices)-1):
        sequence = tuple(entire_sequence[start:i])
        start += 1
        sequences[sequence].append(prices[i])


def get_prices(secret_num, no_generate):
    prices = [secret_num % 10]
    for _ in range(no_generate):
        res = secret_num * 64
        secret_num = mix(res, secret_num)
        secret_num = prune(secret_num)
        div_sn = secret_num // 32
        secret_num = mix(div_sn, secret_num)
        secret_num = prune(secret_num)
        mul_sn = secret_num * 2048
        secret_num = mix(mul_sn, secret_num)
        secret_num = prune(secret_num)
        prices.append(secret_num % 10)
    return prices


# pentru fiecare numar, pentru fiecare secventa de 4,
# calculez pretul, iau max de la fiecare secventa,
# fac suma lor, daca gasesc o secventa cu suma mai mare,
# secventa respectiva devine max seq


for num in numbers:
    num_prices = get_prices(num, 2000)
    get_sequences(num_prices)

max = 0
max_sequence = None

for sequence, bananas in sequences.items():
    sequance_bananas = sum(bananas)
    if sequance_bananas <= max:
        continue
    else:
        max = sequance_bananas
        max_sequence = sequence
print(max_sequence)
