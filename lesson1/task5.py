# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

alphabet = string.ascii_letters

number = int(input('Введите номер буквы: '))
if number > 24:
    number = number % 24
letter = alphabet[number]
print(f'Ваша буква "{letter.title()}"')
