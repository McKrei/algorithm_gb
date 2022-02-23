'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия. 
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, 
чья прибыль выше среднего и ниже среднего.
'''
from collections import Counter, OrderedDict


count_cupany = int(input('Количество компаний: '))
all_company = Counter({})

def create_new_company(i):
    while i > 0:
        name = input('Название компании: ')
        all_company.update({name: 0})
        for _ in range(1, 5):
            all_company[name] += int(input(f'Прибыль за {_} квартал: '))
        i -= 1

create_new_company(count_cupany)
avg = sum(all_company.values())/count_cupany
sorted_company = OrderedDict(sorted(all_company.items(), key=lambda x: x[1]))

for k, v in sorted_company.items():
    if v < avg:
        print(f'Прибыль компании {k}, ниже среднейго {v}')
    else:
        print(f'Прибыль компании {k}, выше среднейго {v}')
        