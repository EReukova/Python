import random
 
number = 2500
 
spisok = ''.join([random.randint(0,9) for _ in range(10)])
spisok = [random.randint(0,9) for _ in range(number)]
spisok = ''.join(list(map(lambda x: str(x), spisok)))
print(spisok)

path = 'data\\' + 'script' + '.txt'
with open(path, 'w', encoding='UTF-8') as file:
    file.write(str(spisok))
 
with open(path, 'r', encoding='UTF-8') as file:
    stroka_1 = list(file.read())
print(stroka_1)
