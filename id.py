import pandas as pd

# Список листов, которые нужно прочитать
sheets = ['Sheet1', 'Sheet2', 'Sheet3']  # Замените на фактические имена листов

# Загрузка данных из всех листов и объединение их в один DataFrame
dfs = []
for sheet in sheets:
    df = pd.read_excel('имя_файла.xlsx', sheet_name=sheet, usecols=['P', 'Z'])
    dfs.append(df)

# Объединение DataFrame'ов из разных листов
combined_df = pd.concat(dfs, ignore_index=True)

# Вывод первых нескольких строк объединенного DataFrame для проверки
print(combined_df.head())

