'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);

проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. 
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
'''
import functools
from sys import getsizeof


def memory(variable):
    global mem
    mem += getsizeof(variable)


def func(number):
    memory(number)
    if number < 2:
        return number
    n = sum_ = 1
    for _ in range(number - 1):
        memory(_)
        n /= -2
        sum_ += n
    memory(sum_)
    memory(n)
    return sum_


def func_2(count, n=1, sum_=1):
    if count < 2:
        return sum_
    n /= -2
    sum_ += n
    memory(count)
    memory(n)
    memory(sum_)
    return func_2(count-1, n, sum_)


@functools.lru_cache()
def func_3(count, n=1, sum_=1):
    if count < 2:
        return sum_
    n /= -2
    sum_ += n
    memory(count)
    memory(n)
    memory(sum_)
    return func_3(count-1, n, sum_)


if __name__ == '__main__':
    mem = 0
    func(100)
    print(f'На 1 вариант, Затратил {mem} памяти')
    mem = 0
    func_2(100)
    print(f'На 2 вариант, Затратил {mem} памяти')
    mem = 0
    func_3(100)
    print(f'На 3 вариант, Затратил {mem} памяти')
    
'''
Очевидно, что рекрсия требует больше памяти, однако мемоизация, которая используеться в lru_cache, тоже требует памяти
Но ее к сожедению посчитать не получилось.
'''