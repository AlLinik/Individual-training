a = [4, 6, 'pу', 'tell', 78]
print('Начальный список №1: ', a)
b = [44, 'hello', 56, 'exert', ['world', 5.7], 3, 6]
print('Начальный список №2: ', b)
# c = a + b         # 1 метод объединения списков
# for i in b:       # 2 метод объединения списков
#     a.append(i)
# print(a)
a.extend(b)         # 3 метод объединения списков
a.insert(3, 6)
print('Объединенный и редактированный НОВЫЙ список:', a)
print('Число 6 в списке встречается', a.count(6), 'раза.')   # 1 способ подсчета элементов
# c = 0                                                      # 2 способ подсчета элементов
# for i in a:
#     if i == 6:
#         c += 1
# print(c)
print(f'Длина списка составляет {len(a)} элементов.')
print('Первый элемент вложенного списка -', a[10][0])

