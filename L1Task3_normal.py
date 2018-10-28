import math
a = int(input("Введите значение a= "))
b = int(input("Введите значение b= "))
c = int(input("Введите значение c= "))
D = b**2 - 4 * a * c
print(D)
if D > 0:
 q = (-b + math.sqrt (D))/(2*a)
 print("x1: ", q)
 q1 = ((-1) * b - math.sqrt(D))/(2*a)
 print("x2: ", q1)        
        
elif D == 0:
 q2 = (-1) * b/(2*a)
 print("Единственный корень: ", q2)
if D < 0:
 print("Дискриминант меньше 0, корней нет")
elif c == 0:
 q4 = (-1) * b // a
 print("x1: 0")
 print("x2: ", q4)
        
        
        

