a = (1, 2, 3, 4, 5, 5, 3)
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
print(b)