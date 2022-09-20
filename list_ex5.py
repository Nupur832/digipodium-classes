names = []
for i in range(5):
    names.append(input("names=>"))

for name in names:
    print(name[::-1])

# 2 wap to print a fibonacci series using the concept of list

fib = [0,1]
for i in range(15):
    fib.append( fib[-1] + fib[-2])
print(fib)

# 3 wap to generate a new list that contains squares of each no. from existing list

x = [1,2,3,3,4,5,2,2]
x2 = []
for num in x:
    x2.append(num ** 2)
print(x)
print(x2)

# 4

x = [1,2,3,3,4,5,6,7]
xodd = []
for i in x:
    if i % 2 != 0:
        xodd.append(i)
print(xodd)

# -------> list comprehension
xodd = [i for i in x if i % 2 != 0]
# -------> list comprehension

# 5
x = [1,2,3,4,2,3,4]
y = [5,7,2,1,3,2,3]
z = []

for i,j in zip(x,y):
    z.append(i + j)
print(x)
print(y)
print(z)

for i in range(1,11):
    print(f'2 * {i} = {2*i}')