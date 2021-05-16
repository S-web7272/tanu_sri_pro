x = [1,6,2,87,9,4,3,0,3,5,3,7,5,3,7,3,3.9,2,5,4,]

#normal 

x3 =[]
for i in x:
    if i % 3 == 0:
        x3.append(i)

#filter with lambda
m3 = lambda i : i % 3 == 0
output = list(filter(m3,x))

#display
print(x)
print(x3)
print(output)