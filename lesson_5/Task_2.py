'''
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [A, 2] и [C, 4, F] соответственно. 
Сумма чисел из примера: [C, F, 1], произведение - [7, C, 9, F, E].
'''

from collections import defaultdict, deque


def dex(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def hex(number):
    num = deque()
    while number > 0:
        d = number % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        number //= 16
    num.reverse()
    return list(num)


signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in signs:
    table[key] += counter
    counter += 1

num_1 = dex(input('Введите первое число: '))
num_2 = dex(input('Введите второе число: '))

print(f'Сумма чисел: {hex(num_1 + num_2)}')
print(f'Произведение чисел: {hex(num_1 * num_2)}')