from helper import read

data = read('pride_n_prejudice.txt')
print(len(data))

newData = data[3:53]
print(newData)

'''
formatting functions
-lower
-upper
-swapcase
-capitalize
-title
-casefold
-ljust
-rjust
-center
'''
print('lower => ',newData.lower())
print('upper => ',newData.upper())
print('swapcase => ',newData.swapcase())
print('capitalize => ',newData.capitalize())
print('title => ',newData.title())
print('casefold => ',newData.casefold())

word = 'Hello'
spacing = 20

ljust = word.ljust(spacing,'*')
print(ljust)
rjust = word.rjust(spacing,'-')
print(rjust)
cen = word.center(spacing,'-')
print(cen)

w='HELLO'
# validation functions - either True or False
print(w.isupper())
print(newData.islower())
print(newData.isalpha())
print(newData.isnumeric())
print(newData.isalnum())

#utility functions
idx = newData.find("Pride")
if idx==-1:
    print('Not found')
else:
    print(f'Pride was found at index {idx}')

idx2 = data.index("in")
print(f'in was found at index {idx2}')

start_idx=0
for i in range(5):
    idx3=data.find('in',start_idx)
    print(f'in was found at {idx3}')
    start_idx=idx3+1

num_of_in = data.count(' in ')
print(f'in occurs {num_of_in} times')