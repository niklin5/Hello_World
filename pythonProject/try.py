a = input("Введите текст со строчной буквы: ")
gl = 0 # гласные
sogl = 0 # согласные
i = ['а', 'о', 'у', 'е', 'ы', 'и', 'я', 'ё', 'э', 'ю']
s = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ъ']
for n in a:
    if n in i:
        gl += 1
for z in a:
    if z in s:
        sogl += 1
if gl == sogl:
    for z in a:
        if z in i:
            print(z)
print (f"Гласные: {gl}, Согласные: {sogl}")




