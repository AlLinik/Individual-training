my_list = [1, 3, 2, 4, 6, 5, 7, 8, 9, 0]
# print('НАЧАЛЬНЫЙ СПИСОК -', my_list)
#
# my_list_replay = []
# for i in my_list:
#     if my_list.count(i) > 1:
#         my_list_replay.append(i)
# print('\nВАРИАНТ 1 (все значения дубликатов) -', my_list_replay)
#
# print('ВАРИАНТ 2 (все значения дубликатов) -', [k for k in my_list if my_list.count(k) > 1])
# print('ВАРИАНТ 3 (элементы, которые имеют дубликаты) -', [j for j in set(my_list) if my_list.count(j) > 1])
print('НАЧАЛЬНЫЙ СПИСОК -', my_list)
my_list_replay = ''
for i in my_list:
    if my_list.count(i) >= 2:
        my_list_replay += str(i)
if my_list_replay != '':
    print(f'В списке ЕСТЬ дубликаты следующих элементов множества - {set(my_list_replay)}')
else:
    print('В списке НЕТ дубликатов')

