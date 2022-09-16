from re import A


x = [1,2,3,2,3,1,5,2,5,1,2,1,1,2,1,2,3,4,5,1,3,2,3,2,4,1,2,1,1,1,3,3,3]

x_one = x.count(1)
x_two = x.count(2)
x_four = x.count(4)
x_five = x.count(5)
print('1 occurred',x_one,'times')
print('2 occurred',x_two,'times')
print('4 occurred',x_four,'times')
print('5 occurred',x_five,'times')

y = [23,45,6,2,21,22,23,32]
z = [1,3,3,5,6,1]

print('x adding y')
x.extend(y)
print(x)
print('x adding z')
x.extend(z)
print(x)

xyz = x + y + z
print(xyz)

a = ['apple','banana','cherry','guava','elaichi']
v = a.pop(3) # pop can remove value from index
print(a)
print(v)
lv = a.pop() # pop remove last value by default
print(a)
print(lv)