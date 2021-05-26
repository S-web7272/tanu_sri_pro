
#funtion 1- take no argument

def my_function():
    '''
    my function very important    ( this is doc funtion)
    '''
    print('my_function,in a list')

my_function()

for i in range(10):
    my_function()

def tanya():
    print('this is a normally name')
    my_function()
    print('this is perfect')
tanya()

def initial():
    '''
    taking input inside a function is super ,
    '''

    x = int(input('enter a number'))
    y = int(input('enter another number'))
    print(x/y)

initial()
