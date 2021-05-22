# wap to create a nested list using user input,the length of list depens  upon the user:

l = int(input('enter the lenght of nested list'))
nested = []
for i in range(l):
    nested.append([])
    k = int(input('enter the list {}'.format(i)))
    for j in range(k):
        nested[i].append(j)
print(nested)