# add each items from 2  list and store result in 3rd list

x = [3,4,5,6,7,8]
y = [22,33,44,66,77,88,99,11]

z = []
for i,j in zip(x,y):
    z.append(i+j)

print(x)
print(y)
print(z)

