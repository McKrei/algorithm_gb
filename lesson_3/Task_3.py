'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
# Решение
from random import randint

list_1 = [randint(1, 99) for _ in range(10)]
min_ind = max_ind = 0
for i in range(1, len(list_1)):
    if list_1[min_ind] > list_1[i]:
        min_ind = i
    if list_1[max_ind] < list_1[i]:        
        max_ind = i
print('Оригинал:\n',list_1)
list_1[min_ind], list_1[max_ind] = list_1[max_ind], list_1[min_ind]
print(f'Поменять местами макс({list_1[min_ind]}) и мин({list_1[max_ind]}):\n',list_1)

    