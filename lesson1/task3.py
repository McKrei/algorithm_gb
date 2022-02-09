# Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.

import random
import string

alphabet = string.ascii_letters

number_one, number_two = map(int, input('Введите два целых числа через пробел: ').split())
random_number = random.randint(number_one, number_two)
print(f'{random_number = }')

number_one, number_two = map(float, input('Введите два числа через пробел: ').split())
random_number = random.uniform(number_one, number_two)
print(f'{random_number = }')

letter_one, letter_two = input('Введите две бувы через пробел: ').lower().split()
ind_1 = alphabet.index(letter_one)
ind_2 = alphabet.index(letter_two)
random_lettor = random.choice(alphabet[ind_1:ind_2+1])
print(f'{random_lettor = }')