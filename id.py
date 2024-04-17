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
