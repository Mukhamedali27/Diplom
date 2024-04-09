from openpyxl import load_workbook

# Указываем путь к файлу Excel
excel_file = 'путь_к_вашему_файлу.xlsx'

# Загружаем файл Excel
wb = load_workbook(excel_file)

# Получаем активный лист
sheet = wb.active

# Создаем словарь для хранения данных вида {P1: [Z1, Z2, ...], P2: [Z1, Z2, ...], ...}
data_dict = {}

# Получаем количество строк и столбцов в таблице
num_rows = sheet.max_row
num_cols = sheet.max_column

# Проходимся по столбцам, начиная с P и считываем значения столбца Z, добавляя их в словарь
for col_num in range(16, num_cols + 1):
    p_col_letter = chr(ord('O') + col_num - 16)  # Получаем букву столбца P
    z_col_letter = chr(ord('Z') + col_num - 16)  # Получаем букву столбца Z
    p_col = sheet[f'{p_col_letter}']  # Получаем столбец P

    # Создаем ключ для словаря
    key = f'P{col_num - 15}'
    
    # Создаем список для хранения значений столбца Z
    z_values = []
    
    # Проходимся по значениям столбца Z и добавляем их в список
    for row in range(1, num_rows + 1):
        z_cell = sheet[f'{z_col_letter}{row}']
        z_values.append(z_cell.value)
    
    # Добавляем данные в словарь
    data_dict[key] = z_values

# Выводим данные
for key, values in data_dict.items():
    print(f'{key}: {values}')

