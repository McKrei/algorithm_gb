# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import string

alphabet = string.ascii_letters

letter_one, letter_two = input('Введите две бувы через пробел: ').lower().split()
ind_1 = alphabet.index(letter_one)
ind_2 = alphabet.index(letter_two)

print(f'''Буква "{letter_one.title()}" в алфавите на {ind_1+1} месте
Буква "{letter_two.title()}" в алфавите на {ind_2+1} месте
Между ними {ind_2-ind_1} букв!
''')