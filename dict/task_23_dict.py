# for key, value in songsdict.items():
#     if len(key) == 4:
#         d = [key, value]
#         print(d)
#     elif len(key) == 5:
#         e = [key, value]
#         print(e)
# dict_1 = dict([(d[0], d[1]), (e[0], e[1])])
# print(dict_1)

# list_songs = []
# for key, value in songsdict.items():
#     if value > 5.0:
#         list_songs += key
#         print(key, end='\n')
songsdict = {'World in My Eyes': 4.76,
             'Sweetest Perfection': 5.43,
             'Personal Jesus': 4.56,
             'Halo': 4.30,
             'Waiting for the Night': 6.07,
             'Enjoy the Silence': 4.6,
             'Policy of Truth': 4.88,
             'Blue Dress': 4.18,
             'Clean': 5.68}
# Вариант 1
print('Общее время звучания песен -', sum(songsdict.values()))
print('Список песен длительностью более 5 минут (1) -', [i for i in songsdict if songsdict[i] > 5])
# Вариант 2
b = []
for key, value in songsdict.items():
    if value > 5.0:
        b.append(key)
print('Список песен длительностью более 5 минут (2) -', b)

print('Словарь песен, название которых состоит из одного слова -',
      {key: songsdict[key] for key in songsdict.keys() if not ' ' in key})





