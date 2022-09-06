for i in range(100):
    print(i, end=' ')

for i in range(10,21):
    print(i, end='x')

for i in range(1,11,2):
    print(i, end='o')

#reverse loop
for i in range(100, 0, -1):
    print(i, end=' ')

print('=>')
data = ['apple','cherry','guava','banana','samosa']
for i,d in enumerate(data):
    print(i, d)

data = ['apple','cherry','guava','banana','samosa']
for i in enumerate(data):
    print(i)

names= ['Apple','Banana','Cherry']
price= [100, 40, 65]

for n, p in zip(names,price):
    print(f'{n} => ${p}')