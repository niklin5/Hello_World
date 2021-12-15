a = (1, 2, 3, 4, 5)
b = int(input('Введите индекс: '))
try:
    a[6]
except IndexError:
    print('Данный индекс не представлен в списке')