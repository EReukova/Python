a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a <= b + c:
    if b <= a + c:
        if c <= a + b:
            if a != b:
                if a != c:
                    print('Треугольник разносторонний')
                else:
                    print('Треугольник равнобедренный')
            elif b != c:
                print('Треугольник равнобедренный')
            else:
                print('Треугольник равносторонний')
else:
    print('Решений нет')
                
                
            
                

                    
