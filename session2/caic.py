a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

deta = b**2 - 4*a*c 
print(deta)

if deta < 0:
    print('vo nghiem')
elif deta == 0:
    print('x1 = x2 =', int(-b/(2*a)))
else:
    x1= (-b+deta**(1/2))/(2*a)
    x2= (-b-deta**(1/2))/(2*a)
    print(f'phuong trinh co 2 nghiem {x2},{x1} ')