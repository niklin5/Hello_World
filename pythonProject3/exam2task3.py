c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
a = 0
b = 0
for i in c_1:
    a += i
for j in c_2:
    b += j
print(a)
print(b)
if a > b:
    print ('Сумма больше в первом кортеже')
else:
    print('Сумма больше во втором кортеже')
print (c_1.index(max(c_1)), c_2.index(max(c_2)), c_1.index(min(c_1)), c_2.index(min(c_2)))
