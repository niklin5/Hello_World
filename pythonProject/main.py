import math

a=input("Введите название фигуры ")
if a=="Прямоугольник":
    q1=float(input("Введите сторону А"))
    q2=float(input("Введите сторону Б"))
    perimeter=(q1+q2)*2
    if q1>0 and q2>0:
        print((q1+q2)*2)
    else:
        print("Неверное значение")
elif a=="Треугольник":
    q3=float(input("Введите длину стороны"))
    perimeter=q3*3
    if q3> 0:
        print(q3*3)
    else:
        print("Неверное значение")
elif a=="Окружность":
    q4=float(input("Введите радиус"))
    perimeter=2*math.pi*q4
    if q4>0:
        print(2*math.pi*q4)
    else:
        print("Неверное значение")
else:
    print("Неверное значение")
