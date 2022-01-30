# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
print(f'Результат побитового И: {first_number & second_number}')
print(f'Результат побитового ИЛИ: {first_number | second_number}')
print(f'Результат побитового XOR: {first_number ^ second_number}')
print(f'Результат побитового сдвига {first_number} на {second_number} знаков в прво: {first_number >> second_number}')
print(f'Результат побитового сдвига {first_number} на {second_number} знаков в лево{first_number << second_number}')