'''
Определение количества различных подстрок с использованием хеш-функции. 
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
'''
import hashlib

def sub_str_count(s):
    result = []
    length = len(s)
    for one in range(length):
        for two in range(one, length + 1):
            # result.append(s[one: two])
            result.append(hashlib.sha1(s[one: two].encode('UTF-8')).hexdigest())
    return len(set(result)) - 1


if __name__ == '__main__':
    print('Уникальных подстрок:', sub_str_count(input('Введите фразу: ')))
