'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. 
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''
from random import randint
import time

my_list = [randint(-100, 99) for i in range(10000)]

def bubble_sorted_revers(array):
    i = 0
    action = True
    while action:
        action = False
        for j in range(len(array) - i - 2):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                action = True
        i += 1
    return array


def bubble_sorted_revers_2(array):
    for i in range(1, len(array) - 1):
        for j in range(len(array) - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

start_time = time.time()
bubble_sorted_revers_2(my_list)
print('1-й вариант', time.time() - start_time)
start_time = time.time()
bubble_sorted_revers(my_list)
print('2-й вариант', time.time() - start_time)