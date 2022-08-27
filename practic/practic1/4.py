a = [2, 1, 1, 2, 3, 4, 4, 5, 'a', 'k', 'c', 'b', 'a']
b = []
for i in a:
    if i not in b:
        b.append(i)
    elif a.count(i) == 2:
        b.remove(i)
print(b)

