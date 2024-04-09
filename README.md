from openpyxl import load_workbook

# Указываем путь к файлу Excel
excel_file = 'путь_к_вашему_файлу.xlsx'

# Загружаем файл Excel
wb = load_workbook(excel_file)

# Получаем активный лист
sheet = wb.active

# Находим столбец P
p_column = None
for col in sheet.iter_cols(values_only=True):
    if col[15] == "P":
        p_column = col
        break

if p_column is None:
    print("Столбец P не найден.")
else:
    # Создаем словарь для хранения данных вида {P1: [Z1, Z2, ...], P2: [Z1, Z2, ...], ...}
    data_dict = {}

    # Итерируемся по строкам, начиная со второй, так как первая строка обычно содержит заголовки
    for row_idx in range(2, sheet.max_row + 1):
        p_value = p_column[row_idx - 1]  # Значение из столбца P
        z_value = sheet[f'Z{row_idx}'].value  # Значение из столбца Z
        if p_value in data_dict:
            data_dict[p_value].append(z_value)
        else:
            data_dict[p_value] = [z_value]

    # Выводим данные
    for key, values in data_dict.items():
        print(f'{key}: {values}')

