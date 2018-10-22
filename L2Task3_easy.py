list = [12, 55, 4, 7, 36, 11, 2, 5]
NewList = []
for x in list:
    if x%2 == 0:
        NewList.append(x / 4)
    else:
        NewList.append(x * 2)
    print(NewList)
    
