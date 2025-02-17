from os import path

FILE_PATH = path.realpath('./input.txt')

with open(FILE_PATH) as f:
    numbers = list(map(int, f.readlines()))


def mix(num: int, secret_num: int) -> int:
    return num ^ secret_num


def prune(secret_num: int) -> int:
    return secret_num % 16777216


nums = []


def get_secret_number(secret_num, no_generate):
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
    return (secret_num)


for num in numbers:
    secret_num = get_secret_number(num, 2000)
    nums.append(secret_num)

print(sum(nums))
