names = [Василий, Петр, Олег, Ольга, Ирина]
salaries = [20000, 45000, 58000, 87254, 49578]
summary = dict(zip(names,salaries))
f = open('salaries.txt', 'w+', encoding='UTF-8')
for key, value in summary.items():
     f.write('{}-{}\n'.format(key,value))
f.close()
f = open('salaries.txt', 'r')
contents = f.readlines()
too_much= 50000
for line in contents:
 k,v = line.split(' - ')
if int(v)<=too_much:
 print('{}-{}'.format(k.upper(), int(int(v)*0.87)))
f.close()
