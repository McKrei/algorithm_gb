'''
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
'''
import cProfile

def test_func(func):
    lst = [0, 1, 0.5, 0.75, 0.625]
    for i, item in enumerate(lst):
        assert func(item) == lst[i]
        print(f'Test {i}, ok')

def func(number):
    if number < 2:
        return number
    n = sum_ = 1
    for _ in range(number - 1):
        n /= -2
        print(f'{n=} {sum_=}')
        sum_ += n
    return sum_



# 1000 loops, best of 5: 913 nsec per loop 10
# 1000 loops, best of 5: 5.99 usec per loop 100
# 1000 loops, best of 5: 693 usec per loop 10_000

# cProfile 1 повторение