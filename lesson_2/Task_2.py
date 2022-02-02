'''
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

def odd_even(number: int):
    odd = even = 0
    for n in str(number):
        if int(n) %2 == 0:
            odd += 1
        else:
            even += 1
    return f'Четных {odd}\nНечетных {even}'

print(odd_even(input('Введите число: ')))
