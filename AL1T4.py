from random import random
m1 = float(input('Введите значение нижней границы диапазона: '))
m2 = float(input('Введите значение верхней границы диапазона: '))
n = random() * (m2-m1) + m1
print(f'{n:.2f}')

from random import random
m1 = int(input('Введите значение нижней границы диапазона: '))
m2 = int(input('Введите значение верхней границы диапазона: '))
n = int(random() * (m2-m1+1)) + m1
print(n)

from random import random
m1 = ord(input('Введите значение нижней границы диапазона: '))
m2 = ord(input('Введите значение верхней границы диапазона: '))
n = int(random() * (m2-m1+1)) + m1
print(chr(n))
