# sum of digit 

number = int(input('enter a digit:'))
total = 0
while number > 0:
    r = number % 10
    total += r
    number = number // 10

print('total',total)    