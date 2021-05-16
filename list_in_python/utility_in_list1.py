x = [12,13,14,16,17,18,88,22,54,76,78,6,34,2,88,]
a = ['alpha','beta','gama']

idx_of_88 = x.index(88)
print('88 occurs at index',idx_of_88)

idx_of_14 = x.index(14)
idx_of_18 = x.index(18)

print('14 occurs at',idx_of_14)
print('18 occurs at',idx_of_18)

# copy logic 
b = a.copy()
print(a,b)

c= a #wrong way of copying a list
print(a,b)

print(a is b)
print(a is c)