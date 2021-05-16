# example, with basic logic
x = [1,2,3,5,88,44,22]

x2= []
for i in x:
    sqr = i**2
    x2.append(sqr)

print(x)
print(x2)

#can be done with comprehension with line

x = [1,2,3,4,5,6,8]

#
x2 = [i**2 for i in x]

print(x)
print(x2)
