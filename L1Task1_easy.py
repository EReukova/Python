n1 = int(input("Введите произвольное число: "))
n2 = 0
while n1 > 0:
    d =  n1 % 10;
    n1 = n1 // 10;
    n2 = n2 * 10;
    n2 = n2 + d
print(n2)



