# wap a find the sum of all odd numbers in a range given by user

end = int(input('enterthe range value'))

#normal code
oddtotal = 0
eventotal = 0

for i in range(end+1):
    if i%2 ==0:
        eventotal += i # eventotal = eventotal+i
    else:
        oddtotal +=i

print('sum of all odds',oddtotal)
print('sum of even',eventotal)

#pythomic 
print('sum of all evens',sum(range(0,end+1,2)))
print('sum of all odds',sum(range(0,end-1,2)))