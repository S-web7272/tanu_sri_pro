# wap to create a nested list using user input,the length of list depens  upon the user:

nested_list=[]
print('enter a value of: ')
while True:
    items = input('enter value >> ').split(',')
    if len(items)>1 and items[0] !=' ':
        nested_list.append(items)
    else:
        break
print(nested_list)