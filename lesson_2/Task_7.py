'''
Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 
1+2+...+n = n(n+1)/2, где n — любое натуральное число. 
'''
number = int(input('Введите число: '))
var1 = 0
for i in range(1, number + 1):
    var1 += i
var2 = int((number * (number + 1)) / 2)
print(f'1+2+...+n = {var1}\nn(n+1)/2 = {var2}')