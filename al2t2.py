n = int(input('Введите число: '))
a = b = 0
while n>0:
    if n%2 == 0:
        a += 1
    else:
        b += 1
    n = n//10
print(f' Четных: {a}; Нечетных: {b}')
