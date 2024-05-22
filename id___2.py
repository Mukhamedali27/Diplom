'''
import re
import sys
def find_ids_in_list(list_of_dicts):
    ids = []
    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            if isinstance(value, str):
                match = re.search(r"Договор \(прямой\) (\d{12})", value)
                if match:
                    ids.append(match.group(1))
    return ids

# Пример использования:
list_of_dicts = sys.argv

ids_found = find_ids_in_list(list_of_dicts)
print("Найденные id:", ids_found)
'''

'''

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
awd = []
awd.append(combined_df)
# Вывод первых нескольких строк объединенного DataFrame для проверки
print(awd)








import pandas as pd

# Read the Excel file, assuming it contains columns P and Z
df = pd.read_excel('C:\\Users\\zhumabek.m\\Desktop\\awd\\febral.xlsx')

# Extract values from columns P and Z and create a list of tuples
data_list = [(row['P'], row['Z']) for index, row in df.iterrows()]

print(data_list)

'''

'''
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



'''







import pandas as pd

# Список листов, которые нужно прочитать
#sheets = ['01032024 381', '1', '2']  # Замените на фактические имена листов
sheets = ['01032024 381']  # Замените на фактические имена листов

# Загрузка данных из всех листов и объединение их в один DataFrame
dfs = []
for sheet in sheets:
    #df = pd.read_excel('C:\\Users\\zhumabek.m\\Desktop\\awd\\febral.xlsx', sheet_name=sheet, usecols=['POLICY_ID','Начисл.доход'])
    df = pd.read_excel('C:\\Users\\zhumabek.m\\Desktop\\awd\\qweqwe.xlsx', sheet_name=sheet, usecols=['POLICY_ID','Начисл.доход'])
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


summed_data = {}
for key, values in sum_dict.items():
    summed_data[key] = sum(values)
print(len(summed_data))
print(summed_data)



'''
# Вывод словаря
print(len(sum_dict))
print(sum_dict) '''
