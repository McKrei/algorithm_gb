'''
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
'''
import cProfile

def test_func(func):
    lst = [1, 1, 0.5, 0.75, 0.625]
    for i, item in enumerate(lst):
        assert func(i) == lst[i]
        print(f'Test {i}, ok')

def func(count, n=1, sum_=1):
    if count < 2:
        return sum_
    n /= -2
    sum_ += n
    return func(count-1, n, sum_)

cProfile.run('func(100)')

# 1000 loops, best of 5: 1.35 usec per loop 10
# 1000 loops, best of 5: 14 usec per loop 100
# Ошибка глубины рекурсии RecursionError loop 10_000 

# cProfile 1 
#  10/1    0.000    0.000    0.000    0.000 Task_1_2.py:12(func) 10 
# 100/1    0.000    0.000    0.000    0.000 Task_1_2.py:12(func) 100
# ...