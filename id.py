my_list = """\
          POLICY_ID  Начисл.доход
0      100010554798    -682300.71
1      100010554798     682301.11
2      100010628565     -74923.23
3      100010900925    -516760.41
4      100010930667    -142741.12
...             ...           ...
99389  100020022924      24597.00
99390  100014665913   -1800000.00
99391  100014665913   -2007616.00
99392  100020089935    1800000.00
99393  100020089935    2007616.00

[99394 rows x 2 columns]
"""

# Разделяем строки по символу новой строки и удаляем первую строку
lines = my_list.split('\n')[1:]

# Удаляем последний элемент списка
lines = lines[:-1]

# Преобразуем каждую строку в список значений
formatted_list = [list(map(lambda x: x.strip(), line.split())) for line in lines]

print(formatted_list)



AttributeError: 'list' object has no attribute 'strip'






my_list = [
    "0      100010554798    -682300.71",
    "1      100010554798     682301.11",
    "2      100010628565     -74923.23",
    "3      100010900925    -516760.41"
]

# Преобразуем каждую строку в список значений
formatted_list = []
for item in my_list:
    parts = item.split()
    parts = [int(parts[0])] + [float(part) for part in parts[1:]]
    formatted_list.append(parts)

print(formatted_list)







import pandas as pd

# Список листов, которые нужно прочитать
sheets = ['01032024 381', '1', '2']  # Замените на фактические имена листов

# Загрузка данных из всех листов и объединение их в один DataFrame
dfs = []
for sheet in sheets:
    df = pd.read_excel('C:\\Users\\zhumabek.m\\Desktop\\awd\\febral.xlsx', sheet_name=sheet, usecols=['POLICY_ID','Начисл.доход'])
    dfs.append(df)

# Объединение DataFrame'ов из разных листов
combined_df = pd.concat(dfs, ignore_index=True)

# Создание словаря
my_dict = {}
for index, row in combined_df.iterrows():
    my_dict[row['POLICY_ID']] = row['Начисл.доход']

# Вывод словаря





print(my_dict)









import pandas as pd

# Список листов, которые нужно прочитать
sheets = ['01032024 381', '1', '2']  # Замените на фактические имена листов

# Загрузка данных из всех листов и объединение их в один DataFrame
dfs = []
for sheet in sheets:
    df = pd.read_excel('C:\\Users\\zhumabek.m\\Desktop\\awd\\febral.xlsx', sheet_name=sheet, usecols=['POLICY_ID','Начисл.доход'])
    dfs.append(df)

# Объединение DataFrame'ов из разных листов
combined_df = pd.concat(dfs, ignore_index=True)

# Создание словаря для хранения сумм для каждого POLICY_ID
sum_dict = {}
for index, row in combined_df.iterrows():
    policy_id = row['POLICY_ID']
    income = row['Начисл.доход']
    if policy_id in sum_dict:
        sum_dict[policy_id].append(income)
    else:
        sum_dict[policy_id] = [income]

# Вывод словаря
print(sum_dict)

