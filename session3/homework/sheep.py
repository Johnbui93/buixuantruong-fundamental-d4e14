# 2.1
flock1 = [5,7,300]
flock2 = [90,24,50,75]
flock = flock1 + flock2
print('hello, my name is John and here is my sheep size')
print(flock)
print(max(flock))
print('now my biggest sheep has size',max(flock),'let shear it')

print('after shearing here is my flock')
aflock = flock1[:]
aflock[2] = 8
print(flock2+aflock)