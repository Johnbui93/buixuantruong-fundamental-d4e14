# age = int(input("your GF age "))

# if age > 18:
#     print('khong bi di tu')
# else:
#     print('boc lich roi')

# grade = int(input("your grade?"))

# if grade == 10:
#     print('xuat sac')
# elif grade >= 9:
#     print('gioi')
# elif grade >= 7:
#     print ('kha')
# elif grade >= 5:
#     print ('trung binh')
# else:
#     print ('yeu')

# number = int(input('your moody '))

# if number >= 60:
#     print('great')
# elif number >=30:
#     print ('sad')
# else:
#     print('cry')

#heigh = int(input('your heigh?'))

# weight, heigh = raw_input().split()

# ybmi = weight/heigh**2

# if ybmi >= 30:
#     print('very overweight')
# elif ybmi >=25:
#     print ('overweight')
# elif ybmi >= 18.5:
#     print('normal')
# else:
#     print('underweight')

a = 1
b = 2
c = 0

deta = b**2 - 4*a*c 
print(deta)

if deta < 0:
    print('vo nghiem')
elif deta == 0:
    print('x1 = x2 =', int(-b/(2*a)))
else:
    print('x1=', (-b+deta**(-1/2))/(2*a), 'x2=',(-b-deta**(-1/2))/2*a )
