'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
'''
from random import randint
from functools import reduce

list_1 = [randint(1, 99) for _ in range(100)]
max_el, min_el = list_1[0], list_1[0]
for el in list_1:
    if max_el < el: max_el = el
    if min_el < el: min_el = el

# Очень прикольно получилось
sum_el = reduce(lambda a, b: a + b, [el for el in list_1 if el != max_el and el != min_el])

print(sum_el)
        
