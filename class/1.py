class new_class:
    def print(self):
        return 'hello'

new_object = new_class()

print(new_object.print())

class B:
    arg = 'Python'
    def g(self):
        return self.arg
b = B()
print(b.g())
print(B.g(b))
b.arg = 'spam'
print(b.g())


# class Rectangle:
#     default_color = "green"
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# rect = Rectangle(10, 20)
# print(rect.width)
# print(rect.height)
# #print(Rectangle.width)   #  не OK
#
# print(Rectangle.default_color)
# print(rect.default_color)   # OK
#
# Rectangle.default_color = "red"
# print(Rectangle.default_color)
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(10, 20)
# print(r1.default_color)
# print(r2.default_color)
#
# r1.default_color = "blue"
# print(r1.default_color)
# print(r2.default_color)
# print(Rectangle.default_color)
