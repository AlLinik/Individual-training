class Name:
    first_name = 'Aliaksandr'    # статистический атрибут класса Name
    def return_name(self):       # return_name - метод (функция) класса Name (пользовательский атрибут)
                                 # self - обязательный аргумент (ключевое слово)
        return self.first_name

print(dir(Name))                 # обзор встроенных и пользовательских атрибутов (свойств, полей) класса

object = Name()                  # Объект (экземпляр) класса Name
print(object.return_name())      # вариант вывода 1
print(Name.return_name(object))  # вариант вывода 2

object.last_name = 'Linik'       # атрибут объекта
print(object.last_name)

object.last_name = 'LINIK'       # замена атрибута объекта
print(object.last_name)
