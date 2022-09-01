class AccessLevels:
    first_name = 'Aliaksandr'
    _last_name = 'Linik'
    __date_birth = '25.12.1986'

    def name_output(self):
        return self.first_name

    def surname_output(self):
        return self._last_name

    def date_birth_output(self):
        return self.__date_birth


my_object = AccessLevels()

print(my_object.name_output())
print(my_object.surname_output())
print(my_object.date_birth_output())


