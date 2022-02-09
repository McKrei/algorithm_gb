# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена». Тяжко было придумать, что то еще, после оптимизации решето!


def get_primes(num):
    if num < 1:
        return num
    begin, end = 2, 128
    while True:
        primes_list = []
        numbers_list = [0, 0] + [n for n in range(begin, end)]
        for i in range(begin, end):
            if numbers_list[i] != 0:
                j = i * 2
                primes_list.append(i)
                if len(primes_list) == num:
                    return i
                while j < end: 
                    numbers_list[j] = 0
                    j += i
        end *= 2

# 1000 loops, best of 5: 11.4 usec per loop 10
# 1000 loops, best of 5: 270 usec per loop 100
# 1000 loops, best of 5: 2.9 msec per loop 1000


def get_primes_v2(num):    
    if num < 1:
        return num
    number = 1
    primes_list = [2]
    while len(primes_list) != num:
        number += 2
        for el in primes_list:
            if number %el == 0:
                break
        else:
            primes_list.append(number)
    return primes_list[-1]

# 1000 loops, best of 5: 2.96 usec per loop 10
# 1000 loops, best of 5: 153 usec per loop 100
# 1000 loops, best of 5: 17.9 msec per loop 1000