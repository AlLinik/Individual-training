# a = [['11', '223'], ['338', '43', '41', '11111']]
# print(a)
# s = ''.join([''.join(i) for i in a])
# # print(s)
# # e = ''.join([''.join(i) for i in s])
# # c = list(e)
# print(s)
# print(list(s))
# b = 0
# for i in s:
#     if i == '1':
#         b += 1
# print(b)

# a = ['11', '223', '338', '43', '41', '11111']
# print(a)
# s = ''.join(a)
# print(s)
# print(list(s))
# b = 0
# for i in s:
#     if i == '1':
#         b += 1
# print(b)

a = [1, 2, 2, 2, 3, 3, 3, 8, 4, 33, 3, 4, 1]
print(a)
s = ''.join(str(a))
print(s)
b = 0
for i in s:
    if i == '3':
        b += 1
print(b)


