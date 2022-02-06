'''
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба минимальны), так и различаться.
'''
from random import randint

list_1 = [randint(1, 100) for _ in range(10)]
ind_min_one, ind_min_two = 0, 0

for i in range(1, len(list_1)):
    if list_1[ind_min_one] > list_1[i]:
        ind_min_one = i
for i in range(1, len(list_1)):
    if i == ind_min_one:
        continue
    elif list_1[ind_min_two] > list_1[i]:
        ind_min_two = i
print(list_1)
print(f'Первойе минимальное: {list_1[ind_min_one]}\nВторое минимальное: {list_1[ind_min_two]}')