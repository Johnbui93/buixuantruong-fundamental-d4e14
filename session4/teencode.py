teencode = {
'nyc':' nguoi yeu cu',
'bf': 'ban than',
'cavl': 'cong an viec lam'

}

While True:
    print('*'*10)
    for i in teencode:
        print(i, end = '\t')
    print()
    code = input('enter your code?')
    if code in teencode:
        print('your code mean:', teencode[code])
    else:
        answer = input('new code? could you explain? y/n')
        print()
        if answer == 'y':
            mean = input('what is this code mean?')
            teencode['code'] = mean
        else:
            break

