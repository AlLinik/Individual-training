sweetshop = {'пирог': ['бисквит', 4.5, 1800],
             'печенье': ['овсяное', 2.5, 2300],
             'конфеты': ['карамель', 3.5, 2500],
             'шоколад': ['молочный', 3.0, 1500],
             'мороженное': ['сливки', 2.0, 3100]}

print('ДОБРО ПОЖАЛОВАТЬ В КОНДИТЕРСКУЮ!!!')

option = input('Что Вас интересует (вся информация, описание , цена, количество)? Введите в строку: ')

if option == 'вся информация':
    for key, value in sweetshop.items():
        print(f'{key} - {value[0]} - {value[1]} - {value[2]}')
elif option == 'описание':
    for key, value in sweetshop.items():
        print(f'{key} - {value[0]}')
elif option == 'цена':
    for key, value in sweetshop.items():
        print(f'{key} - {value[1]}')
elif option == 'количество':
    for key, value in sweetshop.items():
        print(f'{key} - {value[2]}')
# else:
#     print('ТАКОГО ВАРИАНТА НЕТ! ПОПРОБУЙТЕ ЕЩЕ РАЗ!')
#     option = input('Что Вас интересует (вся информация, описание , цена, количество)? Введите в строку: ')
#     if option == 'вся информация':
#         for key, value in sweetshop.items():
#             print(f'{key} - {value[0]} - {value[1]} - {value[2]}')
#     elif option == 'описание':
#         for key, value in sweetshop.items():
#             print(f'{key} - {value[0]}')
#     elif option == 'цена':
#         for key, value in sweetshop.items():
#             print(f'{key} - {value[1]}')
#     elif option == 'количество':
#         for key, value in sweetshop.items():
#             print(f'{key} - {value[2]}')
#     else:
#         print('У ВАС НЕ ПОЛУЧИЛОСЬ! НАМ ОЧЕНЬ ЖАЛЬ! До свидания.')
#         exit()
sum_total = 0
while True:
    product = input('Введите товар из списка выше, который хотите купить, или "нет" (для выхода): ')
    if product == 'нет':
        break
    elif product not in sweetshop:
        print('Такого товара нет в наличии, выберите другой товар!')
        continue
    quantity = int(input('Введите количество товара в граммах: '))
    if quantity > sweetshop[product][2]:
        print('Такого количества товара нет, выберите другое количество или другой товар!')
        continue
    sum_total += quantity * sweetshop[product][1]
    sweetshop[product][2] -= quantity
print(f'Сумма покупки {sum_total}.')
print('ОСТАТОК ТОВАРА:')
for key, value in sweetshop.items():
    print(f'{key} - {value[0]} - {value[1]} - {value[2]}')
print('До свидания.')



