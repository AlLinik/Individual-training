a = [1, 2, 1, 3, 1, 'a', 'l', 'e', 'x']
b = [7, 8, 9]

print(a)

# a.append(4)   # 4 - новый элемент, который добавится в конце строки
# print(a)
# a.insert(2, 5)   # 2 - индекс строки, 5 - новый элемент, который добавится в строку на место с индексом [2]
# print(a)
# a[1] = 6   # 6 - новый элемент ВМЕСТО элемента с индексом [1] в строке
# print(a)
# b.extend(a)   # добавляет список b в конец списка a
# print(b)
# a.extend(b)   # добавляет список b в конец списка a
# print(a)
# c = a + b   # список a - первый, список b - второй
# c = b + a   # список b - первый, список a - второй
# print(c)
# a.remove(1)   # удаляет первое вхождение элемента, даже если их 2
# print(a)
# a.remove()   # ошибка
# a.remove(112)   # ошибка
# a.pop(1)   # удаляет элемент в строке, которому присвоет индекс в скобках
# print(a)
# a.pop(2)    # удаляет последний элемент в строке
# print(a)
# a.pop(112)    # ошибка
# print(a.count(1))

# d = a.copy()   # копируется список
# a.append(5)
# d.append(3)
# print(a)
# print(d)

# a.clear()   # удаляет список (он становится пустым)
# print(a)

# a.reverse()   # разворачивает список (он становится противоположным)
# print(a)

# e = [1, 22, 5, 53, 7, 17, 14]   # сортирует по возрастанию
# e.sort()
# print(e)

# e = [1, 22, 5, 53, 7, 17, 14]   # сортирует по убыванию
# e.sort(reverse=True)
# print(e)

# print(len(a))   # подсчитывает количество элементов в списке

list.copy(a)
print(a)