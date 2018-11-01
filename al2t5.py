n = int(input('Введите число: '))
s = 0
for i in range(1, n+1):
    s += i
m = n * (n + 1) // 2
if s == m:
    print('Равенство верно')
else:
    print('Равенство не верно')
