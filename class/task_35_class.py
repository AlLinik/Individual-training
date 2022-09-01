class Name:

    # статические поля класса Name
    first_name = 'Aliaksandr'         # статическая переменная 1 класса Name
    last_name = 'Linik'               # статическая переменная 2 класса Name

    def __init__(self, month, day):   # метод инициализации (инициализатор)

        # динамические поля объекта object_name
        self.month = month            # динамическая переменная 1 объекта object_name
        self.day = day                # динамическая переменная 2 объекта object_name

object_name = Name('december', 25)    # Объект (экземпляр) класса Name

print(object_name.first_name)
print(object_name.last_name)
print(object_name.month)
print(object_name.day)
