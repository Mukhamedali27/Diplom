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


'''

import pandas as pd
df = pd.read_excel('158.xlsb')


column_P_values = df['P'].tolist()
column_Z_values = df['Z'].tolist()



print("Значения из столбца P:", column_P_values)
print("Значения из столбца Z:", column_Z_values)



