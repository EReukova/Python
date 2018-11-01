print("Ноль в качестве знака операции завершит работу программы")

while True:
        s = input("Знак (+,-,*,/): ")
        if s == '0': break
        if s in ('+','-','*','/'):
                x = float(input("x = "))
                y = float(input("y = "))
                if s == '+':
                        print(f'Искомое значение: {x+y:.2f}')
                elif s == '-':
                        print(f'Искомое значение: {x-y:.2f}')
                elif s == '*':
                        print(f'Искомое значение: {x*y:.2f}')
                elif s == '/':
                        if y != 0:
                                print(f'Искомое значение: {x/y:.2f}')
                        else:
                                print("Деление на ноль!")
        else:           
                print("Неверный знак операции!")
