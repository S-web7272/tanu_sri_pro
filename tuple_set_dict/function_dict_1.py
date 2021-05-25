##function_list
#update
#pop
#popitem
#get
#keys
#values
#items
#clear


fruits = {'apple':50,'banana':30,
    'cherry':200,'dragonfruits':250}

print('updating values in dict')

new_fruits = {'mango':150,'grapes':80}
fruits.update(new_fruits)
print(fruits)

print('removing value from dict')

fruits.pop('cherry')
print(fruits)

#better vresion
if 'orange' in fruits:
    fruits.pop('orange')
    print(fruits)
else:
    print('orange not found')

last_item_removed = fruits.popitem()
print(fruits)
print(f'{last_item_removed} removed from fruits')

# accessing value from dict
print(fruits['apple'])


# better version to access value from dict
print('using the get method in dict')
print(fruits.get('apple'))
print(fruits.get('Apple'))

print('using the get() with default value, in dict')
print(fruits.get('apple','price not found'))
print(fruits.get('Banana','price not found'))

#accessing  keys, values and pair wise items in dict
print(fruits.values())
print(fruits.keys())
print(fruits.items())

print('looping in dict')
print('=> normal loop get only keys')

for i in fruits:
    print(i)

print('=> get only value')
for i in fruits.values():
    print(i)

#another way to get values

print('=> get both key and value')
for k,v in fruits.items():
    print(k,'-->',v)

    