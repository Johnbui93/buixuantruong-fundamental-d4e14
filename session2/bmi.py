heigh = int(input('your heigh?'))
weight = int(input('your weight'))

ybmi = weight/heigh**2

if ybmi >= 30:
    print('very overweight')
elif ybmi >=25:
    print ('overweight')
elif ybmi >= 18.5:
    print('normal')
else:
    print('underweight')