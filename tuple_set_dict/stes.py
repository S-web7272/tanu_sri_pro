x = {1,2,3,4,5}
y = {'apple','banana','mango'}
z = {2,5,7,6,4,9,4,6,9,2,5,5,6,4,6,87,65,5,3}


print(x)
print(y)
print(z)
print(type(z))

a = [1,2,3,4,5,6,7,8,9] #list
b = (1,2,3,4,5,6,7,8,9) #tuple

#list - set - tupole are interconvertible
a_set = set(a)
b_set = set(b)
print(a,a_set)
print(b,b_set)

# set value  connot be indexed or sliced

for i in a_set:
    print(i,end=' ')
    