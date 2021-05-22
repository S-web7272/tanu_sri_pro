# wap to generate a list of cricketers entered by user  only if the first letter of the name is capital.the size will depend upon user:

cricketers = []
while True:
    name = input('cricketers name: ')
    if not name:
        break
    elif name[0].isupper():
        cricketers.append(name)
    print(cricketers)