'''
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
'''

def summa(number):
    n = sum_ = 1
    for _ in range(number):
        n /= -2
        sum_ += n
    return sum_

print(summa(int(input('Введите число: '))))    