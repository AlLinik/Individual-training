class Name:
    arg = 'ALIAKSANDR'
    def return_name(self):
        return self.arg

object_name = Name()

print(object_name.return_name())      # вариант вывода 1
print(Name.return_name(object_name))  # вариант вывода 2

# замена аргумента
object_name.arg = 'LINIK'
print(object_name.return_name())

