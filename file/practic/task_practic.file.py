# f = open('text_practic.txt', 'r')
# d = []
# for i in f:
#     i = i.strip("\n")
#     # i = i[:-1]   # удаляет последнюю букву последнего слова, если не было переноса
#     d.append(i)
# print(f'Элементы в text_practic.txt - {d}')
# print(f'Количество элементов (строк) в text_practic.txt - {len(d)}')
# print(f'''
# Длина элемента №1 в text_practic.txt - {len(d[0])}
# Длина элемента №2 в text_practic.txt - {len(d[1])}
# Длина элемента №3 в text_practic.txt - {len(d[2])}
# Длина элемента №4 в text_practic.txt - {len(d[3])}
# Длина элемента №5 в text_practic.txt - {len(d[4])}''')
# f.close()

# # ВАРИАНТ 2
# f = open('text_practic.txt', 'r')
# counter = 0
# str_txt = ''
# for i in f.readlines():
#     counter += 1
#     str_txt += str(i)
# str_txt = str_txt.split('\n')
#
# print(f'Количество элементов (строк) в text_practic.txt - {counter}')
# print(f'Элементы в text_practic.txt - {str_txt}')
# print(f'''
# Длина элемента №1 в text_practic.txt - {len(str_txt[0])}
# Длина элемента №2 в text_practic.txt - {len(str_txt[1])}
# Длина элемента №3 в text_practic.txt - {len(str_txt[2])}
# Длина элемента №4 в text_practic.txt - {len(str_txt[3])}
# Длина элемента №5 в text_practic.txt - {len(str_txt[4])}''')
# f.close()

#Вариант 3
f = open('text_practic.txt', 'r')
counter = 0
str_txt = ''
for i in f.readlines():
    counter += 1
    str_txt += str(i)
    if i[-1] == '\n':
        i.replace('\n', '')
str_txt = str_txt.split()
print(f'Количество элементов (строк) в text_practic.txt - {counter}')
print(f'Элементы в text_practic.txt - {str_txt}')
print(f'''
Длина элемента №1 в text_practic.txt - {len(str_txt[0])}
Длина элемента №2 в text_practic.txt - {len(str_txt[1])}
Длина элемента №3 в text_practic.txt - {len(str_txt[2])}
Длина элемента №4 в text_practic.txt - {len(str_txt[3])}
Длина элемента №5 в text_practic.txt - {len(str_txt[4])}''')
f.close()

