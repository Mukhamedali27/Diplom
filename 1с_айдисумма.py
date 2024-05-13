
import re
import csv
def find_ids_in_list(list_of_dicts):
    ids = []
    for dictionary in list_of_dicts:                                      # Проход по каждому словарю в списке
        for key, value in dictionary.items():                             # Проход по каждой паре ключ-значение в словаре
            if isinstance(value, str):                                    # Проверка, является ли значение строкой
                match = re.search(r"Договор \(прямой\) (\d{12})", value)  # Поиск совпадения с регулярным выражением
                if match:                                                 # Если найдено совпадение
                    ids.append(match.group(1))
                    break
    return ids


li =[]
column_O_values =[]
with open("C:\\Users\\zhumabek.m\\Desktop\\awd\\1С-01.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        my_dict = dict(enumerate(row))
        li.append(my_dict)
        #print(my_dict)
    ids_found = find_ids_in_list(li)

#liii = [ids_found[i] for i in range(len(ids_found)) if i == 0 or ids_found[i] != ids_found[i-1]]
#print("Найденные id:", ids_found)



import csv

Sample = []
with open("C:\\Users\\zhumabek.m\\Desktop\\awd\\1С-01.csv", encoding="ANSI") as V:
    SR = csv.reader(V, delimiter=';')
    for col in SR:
        Sample.append(col[14])

list3 = [f'{ids_found[i]}:{Sample[i+1]}' for i in range(min(len(ids_found), len(Sample)))]

print(list3)
#print(len(ids_found),len(Sample))


