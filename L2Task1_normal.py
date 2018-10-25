list = [12, 55, 4, 7, 36, 11, 2, 5]
NewList = []
for x in list:
    if x > 0:
     y = math.sqrt(x)
    if y % int(y) == 0:
     NewList.append(y)
    print(NewList)
    
