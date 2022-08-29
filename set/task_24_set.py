# Создайте множество цветов, произрастающих одновременно в саду и на лугу

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
my_garden = set(garden)
print('Цветы в саду: ', my_garden)

meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
my_meadow = set(meadow)
print('Цветы на лугу: ', my_meadow)

print('\nЦветы, произрастающие одновременно в саду и на лугу (1): ', my_garden.intersection(my_meadow))
print('Цветы, произрастающие одновременно в саду и на лугу (2): ', my_meadow & my_garden)
