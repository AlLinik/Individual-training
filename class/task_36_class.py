class Methods:
    name1 = 'method'
    string1 = 'class method'

    @staticmethod
    def static_method(a, b):
        name2 = 'class Methods'
        print('static method', name2)
        return a + b
    @classmethod
    def class_method(cls, string2):
        cls.string2 = string2
        name3 = 'class Methods'
        print('class method', name3)
        return cls.string1 + string2
    def method_object(self, string3):
        self.string3 = string3
        print('method object', string3)
        return self.name1 + ' object class Methods'

my_object = Methods()

print(Methods.static_method('static method', ' class Methods'))
print(Methods.class_method(' class Methods'))
print(my_object.method_object('class Methods'))

