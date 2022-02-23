'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, 
делящий его на две равные части: в одной находятся элементы, 
которые не меньше медианы, в другой — не больше медианы.
'''

from random import randint
from statistics import median

arr_len = 10
my_list = [randint(1, 100) for _ in range(arr_len * 2 + 1)]

def my_median(array):
    avg = int(len(array) / 2)
    for j in range(avg + 1):
        min_ind = j
        for i in range(j + 1, len(array)):
            if array[min_ind] > array[i]:
                min_ind = i
        array[j], array[min_ind] = array[min_ind], array[j]


    return array[avg]

print('Мой результат', my_median(my_list))
print('Проверка', median(my_list))


