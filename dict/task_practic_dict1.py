# Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.

cars = {'BMW': ['X3', 'X5', 'X6'], 'Tesla': ['Model S', 'Model X', 'Model Y']}
print('1 и 3 значение словаря "BMW": ', cars['BMW'][0], '-', cars['BMW'][2])
print('1 и 3 значение словаря "Tesla": ', cars['Tesla'][0], '-', cars['Tesla'][2])

a = {'a':1, 'm':2 }
b = a.items()
print(b)
for i in a:
    print(i)