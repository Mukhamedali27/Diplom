[          POLICY_ID  Начисл.доход
0      100010554798    -682300.71
1      100010554798     682301.11
2      100010628565     -74923.23]


['100019131522:-28396,62', 
 '100017975432:690', '100019645714:-20433,02', '100019475027:-9222,89', 
 '100019280154:-30861,65', '100018681662:-18568,08', '100019651828:-14546,19']

data1 = [
    [0, 100010554798, -682300.71],
    [1, 100010554798, 682301.11],
    [2, 100010628565, -74923.23]
]

data2 = [
    '100019131522:-28396,62',
    '100017975432:690',
    '100019645714:-20433,02',
    '100019475027:-9222,89',
    '100019280154:-30861,65',
    '100018681662:-18568,08',
    '100019651828:-14546,19'
]

# Создаем словарь для хранения сумм по каждому id из второго списка
sum_by_id = {}

# Вычисляем суммы для каждого id из первого списка
for item in data1:
    index, id_, amount = item
    if id_ in sum_by_id:
        sum_by_id[id_] += amount
    else:
        sum_by_id[id_] = amount

# Сравниваем суммы для каждого id из второго списка и записываем результат в третий список
result = []
for item in data2:
    id_, amount = item.split(':')
    amount = float(amount.replace(',', '.'))
    id_ = int(id_)
    
    if id_ in sum_by_id:
        if abs(sum_by_id[id_] - amount) > 0.01:  # Проверка на разницу в 0.01 (из-за погрешности при работе с float)
            result.append(f'{id_}:{sum_by_id[id_]}')
    else:
        result.append(f'{id_}: not found')

print(result)







import pandas as pd

# Чтение данных из первого листа
df1 = pd.read_excel('имя_файла.xlsx', sheet_name='Лист1')

# Чтение данных из второго листа
data_list = ['100019131522:-28396,62', 
             '100017975432:690', 
             '100019645714:-20433,02', 
             '100019475027:-9222,89', 
             '100019280154:-30861,65', 
             '100018681662:-18568,08', 
             '100019651828:-14546,19']

# Преобразование списка строк в DataFrame
data_tuples = [tuple(item.split(':')) for item in data_list]
df2 = pd.DataFrame(data_tuples, columns=['POLICY_ID', 'Начисл.доход'])

# Приведение типа данных в df2 к тому же, что и в df1
df2['POLICY_ID'] = df2['POLICY_ID'].astype(int)

# Сравнение сумм по идентификаторам
diff_df = pd.merge(df1, df2, on='POLICY_ID', suffixes=('_1', '_2'))
diff_df['Начисл.доход_1'] = diff_df['Начисл.доход_1'].astype(float)
diff_df['Начисл.доход_2'] = diff_df['Начисл.доход_2'].str.replace(',', '.').astype(float)
diff_df['Разница'] = diff_df['Начисл.доход_1'] - diff_df['Начисл.доход_2']

# Разделение данных на два DataFrame по условию различия сумм
df_diff_1 = diff_df[diff_df['Разница'] != 0][['POLICY_ID', 'Начисл.доход_1']]
df_diff_2 = diff_df[diff_df['Разница'] != 0][['POLICY_ID', 'Начисл.доход_2']]

# Запись данных на новые листы
with pd.ExcelWriter('output.xlsx') as writer:
    df_diff_1.to_excel(writer, sheet_name='Несоответствие_1', index=False)
    df_diff_2.to_excel(writer, sheet_name='Несоответствие_2', index=False)

