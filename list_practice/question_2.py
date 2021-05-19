#wap to create a list of name and then remove name that contain 'a' or 'o' char:

names = ['ravi','suman','dev','laajo','karan','adhiraj','tanu','sumo']

names_containing_a = [name for name in names if 'a' in name]
names_containing_o = [name for name in names if 'o' in name]

print(names_containing_a)
print(names_containing_o)


