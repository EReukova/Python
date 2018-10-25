number = int(input("Введите произвольное число: "))
result = 0
while number > 0:
    remainder =  number % 10;
    number = number // 10;
    result = result * 10
    result = result + remainder

print(result)



