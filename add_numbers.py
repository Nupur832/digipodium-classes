ans = 0

while True:
    num = input('enter a number: ')
    if num.isnumeric():
        ans += int(num)
    else:
        break
print('total =',ans)

      