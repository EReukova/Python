import random
list = [random.randint(-5,50) for _ in range(10)]
print(list)
result = [x for x in list if x % 3 == 0 and x % 4 != 0]
print(result)
