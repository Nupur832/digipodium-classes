# 1
my_string = 'Hello World'
print(my_string)

my_string = "Hello World"
print(my_string)

my_string = '''Hello World'''
print(my_string)

# 2
str = "digipodium"
print(len(str))

# 3
str = input("Enter your string: ")
word = str.split()
print(word[-1])

# 4
my_string = '''Python
Is
Everywhere.'''
print(my_string)

# 5
str = []
for i in range(1):
    str.append(input("names=>"))

for name in str:
    print(name[::-1])

# 6
str = 'how are you?'
print(str.upper())

str = 'How Are You?'
print(str.upper())

# 7
str = 'HOW IS IT GOING?'
print(str.lower())

str = 'How Is It Going?'
print(str.lower())

# 8
words = ['Python','is','easy','to','learn']
content = " ".join(words)
print(content)

# 9
my_string = '''The only way to 
learn the program is 
by writing code.'''
print(my_string)

# 10
my_string = "to move to newline '\\n' is used"
print(my_string)

# 11
a = 15
print("The variable is ",a)

# 12
s1 = 'python'
s2 = 'is'
s3 = 'great'
s4 = s1 + s2 + s3
print(s4)
s5 = s1 + ' ' + s2 + ' ' + s3 
print(s5)

# 13
print('#' * 20)

# 14
for i in range(1,10):
    print(i,'.',sep = ' ')

# 15
sentence = input("Enter a sentence: ")
print( * sentence.split(" "), sep = '\n')

# 16
my_string = input('Enter a string: ')
print(my_string.endswith('?'))

# 17
x = input("Enter a string: ")
num_of_in = x.count('e')
print(f'e occurs {num_of_in} times')

# 18
num = input("Enter a number: ")
if num.isdigit():
    print("It is a number")
    user_inp = int(num)
else:
    print("It is not a number")

# 19
text = '    This is not a good string     '
cleaned_text = text.strip()
print(cleaned_text)

# 20
text = input('Enter a sentence: ')
if text.isupper():
    print("Found")
else:
    print("Not found")

# 21
names = 'Joe, David, Mark, Tom, Chris, Robert'
my_string = []
my_string = names.split(',')
print(my_string)

# 22
text = 'This is some text'
a = text.split()
a.insert(1,'aye')
a.insert(3,'aye')
a.insert(5,'aye')
a.insert(7,'aye')
print(a)

# 23
txt = input("Enter a string: ")
if 'fyi' in txt:
    print("Yes,it is present")
else:
    print("No,it is not present")

# 24
text = '%p34@y!*-*!t68h#&on404'
from string import punctuation
for p in punctuation:
    text = text.replace(p, ' ')
from string import digits
remove_digits = str.maketrans('','',digits)
res = text.translate(remove_digits)
print(res)

# 25
sentence = input("Enter the sentence: ")
words = sentence.split()
count = 0
sum = 0
for x in words:
    sum += len(x)
    count += 1
total = sum / count
print(total)




