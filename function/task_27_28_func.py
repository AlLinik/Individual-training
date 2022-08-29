def function(*args, **kwargs):
    print(f'Позиционные (нечетные индексы) - {args[1::2]}')
    for key, value in kwargs.items():
        if isinstance(value, str):   # можно - if value == str(value):
            print('Ключевой аргумент, значение которого строка -', key)

function(1, 2, 3, 4, 5, a=6, b='hello', c=8, d='world', e=10)

# print(f'Ключевые (значения - строки) - {[value for value in kwargs.values() if value == str(value)]}')

                                                          #   [можно так: ... if isinstance(value, str)]

















