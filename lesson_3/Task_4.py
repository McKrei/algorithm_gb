'''
Определить, какое число в массиве встречается чаще всего.
'''
from random import randint

def count_namber(l: list):
    number = l[0]
    max_count = 1
    for i in set(l):
        count = 0

        for j in l:
            if i == j:
                count += 1

        if count > max_count:
            number, max_count = i, count

    if max_count == 1:
        return 'Все числа уникльны'
    else:
        return f'Число {number} встретилось {max_count} раз'

if __name__ == '__main__':
    my_list = [randint(1, 99) for _ in range(1_000)]
    print(count_namber(my_list))
