'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
from random import randint

my_list = [randint(-999_999, 999_999) for _ in range(100_000)]
negative_list = [el for el in set(my_list) if el < 0]
if len(negative_list) > 0:
    max_negative_number = negative_list[0]
    for el in negative_list:
        if max_negative_number > el:
            max_negative_number = el
    print('Вы загадали:', max_negative_number)
else:
    print('Нет отрицательных элементов')