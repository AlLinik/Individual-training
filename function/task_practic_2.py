def function_counting(data_type):
    if type(data_type) == tuple:
        tuple_str = ''
        for i in data_type:
            if i == str(i):
                tuple_str += i
        print(f'Длина всех слов кортежа - {len(tuple_str)}')
    elif type(data_type) == list:
        count_int = 0
        count_str = 0
        for i in str(data_type):
            if i.isdigit():
                count_int += 1
            elif i.isalpha():
                count_str += 1
        print(f'\nКоличество чисел в списке - {count_int}')
        print(f'Количество букв в списке - {count_str}')
    elif type(data_type) == int:
        count = 0
        for i in str(data_type):
            if int(i) % 2 != 0:
                count += 1
        print(f'\nКоличество нечетных цифр в числе - {count}')
    elif type(data_type) == str:
        count = 0
        for i in data_type:
            count += 1
        print(f'\nКоличество букв в строке - {count}')

function_counting((1, 2, 3, 'hello', 'world'))
function_counting([1, 2, 3, 'hello', 'world'])
function_counting(123456789)
function_counting('overone')


