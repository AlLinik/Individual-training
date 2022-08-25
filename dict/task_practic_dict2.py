# list_1 = ['a', 'b', 'c', 'd', 'e']
# list_2 = [1, 2, 3, 4, 5]
# dict_number_2 = dict(zip(list_1, list_2))
# print(dict_number_2)
# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

dict_number_1 = {a: a for a in range(1, 6)}
print('Исходный словарь: ', dict_number_1)

print('Вариант 1: ', dict_number_1[1] * dict_number_1[2] * dict_number_1[3] * dict_number_1[4] * dict_number_1[5])

count = 1
for i in dict_number_1:
    count = count * dict_number_1[i]
print('Вариант 2: ', count)

