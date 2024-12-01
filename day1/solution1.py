from os import path
file_path = path.realpath('day1/input.txt')

SEPARATOR = "   "

with open(file_path) as f:
    file_content = f.readlines()


list1 = []
list2 = []
for line in file_content:
    list1.append(int(line.split(SEPARATOR)[0].strip()))
    list2.append(int(line.split(SEPARATOR)[1].strip()))

list1.sort()
list2.sort()

total_distance = 0
for id_1, id_2 in zip(list1, list2):
    difference = id_1 - id_2
    total_distance += abs(difference)

print(total_distance)
