# datatypes => python has 9 basics types

# integer (int)
a = 1 
b = 23789034
c = +2345
d = -2567

print(type(a),type(b),type(c),type(d))

# float
a = 1.7 
b = -5.874556
c = .23453454211113434
d = 1.3e-30

print(type(a),type(b),type(c),type(d))

#bool
a = True
b = False
c = a and b
d = a or b 

print(type(a),type(b),type(c),type(d))

#string - (str)
a = 'hockey' 
b =  "bollyboll"
c =  ''' can i play cricket'''
d =  """hello
hee
who
typing
string
"""

print(type(a),type(b),type(c),type(d))

# Nonetype - none

a = None
b = None
print(type(a),type(b))
z = None
print(z)

# data - structure

# list -> square brackets
a = [1,2,3,4,5,6]
print(type(a))

# tuple -> round brackets
a = (1,2,3,4,5,6)
b = 1,8,9,5,6,
print(type(a),type(b))

# set -> curly braces
a = {1,2,3,4,5,6}
b = {1,9,6,5,7,1,5,9,2,3,4,5,54,21,7}
print(type(a),type(b))

# dict -> curly braces
a = {"name":'tanu','price':400}
b = {1:1000,2:2000,3:3000}
print(type(a),type(b))

# programmatically check type -

a = 10 
out = isinstance(a, int)
print("is an integer => ",out)
out = isinstance(a, float)
print("is a float =>",out)

price = input('enter the price of mouse you bought:')
print(isinstance(price,int))
print(isinstance(price,float))
print(isinstance(price,str))




