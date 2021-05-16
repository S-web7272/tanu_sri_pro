fname = 'smita'
lname = 'sri'

# concatenation - joining strings together

fullname = fname + ' ' + lname + ' is the name '
print(fullname)

#duplication - cloning the string

word = 'hi'
print(word * 3)
print('-|-'* 2)
print('/' * 25)

for  i in range(1,10):
    print('$ ' * i)

# membership operator
massage = ' the most important thing for a coder is to code'

if 'thing' in massage:
    print('thing -> word found')

if 'very' in massage:
    print('very -> word found')

if 'b' not in massage:
    print('b is not available in massage')

print('elephant'in massage)