x = (1,2,3,4,5)
y = 15,18,19

print(x)
print(y)
print(type(x))
print(type(y))

a = [2,8,23,9,45]
at = tuple(a)
print('list =>',a, 'tuple =>', at)

name = 'alibagh'
names = tuple(name)
print('string =>',name ,  'tuple =>', names)

a = 4 
b = 8
c = 6
d = a,b,c
print(d)

# error => d[3] = 10

#function
#count
#index
a = (1,2,3,4,5,5,7,6,45,34,23,76,98,56,34,54,12,15,4,5,6)
print("counting aal 3s =" ,a.count(3))
print("index of 45 = " , a.index(45))