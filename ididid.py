

import pandas as pd

df = pd.read_csv("C:\\Users\\zhumabek.m\\Desktop\\awd\\1C-01.csv")

print(df.to_string()) 











'''
data1 = [
    [0, 100010554798, -682300.71],
    [1, 100010554798, 682301.11],
    [2, 100019645714, -74923.23]
]

data2 = [
    '100019131522:-28396,62',
    '100017975432:690',
    '100019645714:-74923.23',
    '100019475027:-9222,89',
    '100019280154:-30861,65',
    '100010554798:682301.11',
    '100010554798:-682300.71'
]

# Создаем словарь для хранения сумм по каждому id из второго списка
sum_by_id = {}

# Вычисляем суммы для каждого id из первого списка
for item in data1:
    index, id_, amount = item
    if id_ in sum_by_id:
        sum_by_id[id_] =amount
    else:
        sum_by_id[id_] = amount
print(sum_by_id)
                         
a = 0
b = 0
# Сравниваем суммы для каждого id из второго списка и записываем результат в третий список
result = []
for item in data2:
    #print(item)
    id_, amount = item.split(':')
    amount = float(amount.replace(',', '.'))
    id_ = int(id_)
    #print(id_)
    if id_ in sum_by_id:
        if abs(sum_by_id[id_] + amount) > 0.01:  # Проверка на разницу в 0.01 (из-за погрешности при работе с float)
            result.append(f'{id_}:{sum_by_id[id_]}')
            a += 1
    else:
        result.append(f'{id_}: not found')
        b +=1

print(result)

print(a,b)
'''
