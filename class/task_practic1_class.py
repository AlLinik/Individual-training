# if type(self.string) == str:
#     vow, vow_str, cons, cons_str = 0, '', 0, ''
#     vowels = 'аеёиоуэюя'
#     for i in self.string:
#         if i not in vowels:
#             cons += 1
#             cons_str += i
#         else:
#             vow += 1
#             vow_str += i
#     if vow * cons <= len(self.string):
#         return vow_str
#     else:
#         return cons_str
#
# elif type(self.string) == int:
#     odd = 0
#     even = 0
#     for i in str(self.string):
#         if int(i) % 2 == 0:
#             even += int(i)
#         else:
#             odd += 1
#     return even * len(self.string)


# def string_or_number(self):
#     for i in self.string:
#         if i.isdigit():
#             odd = 0
#             even = 0
#             for j in str(self.string):
#                 if int(j) % 2 == 0:
#                     even += int(j)
#                 else:
#                     odd += 1
#             return even * len(self.string)
#         elif i.isalpha():
#             vow, vow_str, cons, cons_str = 0, '', 0, ''
#             vowels = 'аеёиоуыэюя'
#             for j in self.string:
#                 if j not in vowels:
#                     cons += 1
#                     cons_str += j
#                 else:
#                     vow += 1
#                     vow_str += j
#             if vow == 0:
#                 return 'Гласных нет. Произведение = 0'
#             elif cons == 0:
#                 return 'Согласных нет. Произведение = 0'
#             elif vow * cons <= len(self.string):
#                 return vow_str
#             return cons_str
class Task:

    def __init__(self, string_or_number):
        self.string_or_number = string_or_number
    def determination_length(self):
        length = len(str(self.string_or_number))
        return length
    def data_input(self):
        if type(self.string_or_number) == str:
            vow, vow_str, cons, cons_str = 0, '', 0, ''
            vowels = 'аеёиоуэюя'
            for i in self.string_or_number:
                if i not in vowels:
                    cons += 1
                    cons_str += i
                else:
                    vow += 1
                    vow_str += i
            if vow * cons <= self.determination_length():
                return vow_str
            else:
                return cons_str
        elif type(self.string_or_number) == int:
            odd = 0
            even = 0
            for i in str(self.string_or_number):
                if int(i) % 2 == 0:
                    even += int(i)
                else:
                    odd += 1
            return even * self.determination_length()
obj = Task(123456789)
print(obj.data_input())

