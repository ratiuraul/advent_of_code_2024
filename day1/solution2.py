import time
from collections import Counter
from os import path
file_path = path.realpath('day1/input.txt')
start_time = time.time()
SEPARATOR = "   "

with open(file_path) as f:
    file_content = f.readlines()

list1 = []
list2 = []
for line in file_content:
    list1.append(int(line.split(SEPARATOR)[0].strip()))
    list2.append(int(line.split(SEPARATOR)[1].strip()))

l1_c = Counter(list1)
l2_c = Counter(list2)

final_score = 0
for key, value in l1_c.items():
    if key in l2_c:
        score = key * value * l2_c[key]
        final_score += score


print("--- %s seconds ---" % (time.time() - start_time))
