
name = "smita" #outside function

def who():
    print('who am i')
    print(f'i am {name}') #can be access inside function

def what():
    print('waht are you there')
    name = 'srivastava'  #python  can not the value of variable  created outside directly
    print(f'i am {name}') # this is just  the local value of name  variable

def update_name():
    global name
    print('old name',name) # this keyword tells  python, that we want to use global variable and also modify value
    name = "tanu" 
    print('new name',name) # this line updates the global variable now

who()
print('global variable =>',name)
what()
print('global variable =>',name)   
update_name()
print('global variable =>', name)