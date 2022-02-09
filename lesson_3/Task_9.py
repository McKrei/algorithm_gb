'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''
from random import randint

matrix = [[randint(1, 100) for _ in range(5)] for _ in range(5)]
print(matrix)
min_in_line = []
for line in matrix:
    min_el = line[0]
    for el in line:
        if min_el > el:
            min_el = el
    min_in_line.append(min_el)

min_el = min_in_line[0]

for el in min_in_line:
    if min_el > el:
        min_el = el

print(min_el)