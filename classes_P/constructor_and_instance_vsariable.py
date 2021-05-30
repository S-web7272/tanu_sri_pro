
class pet:
    name = 'minnu'
    age = 3
    pettype = 'cat'


p1 = pet()
p2 = pet()
print(p1.name,p1.pettype,p1.age)
print(p2.name,p2.pettype,p2.age)


class pet:
    def __init__(self, name, pettype,age):
        #instance variables(object variables)
        self.name = name
        self.pettype = pettype
        self.age = age


p1 = pet('minnu','dog',10)
p2 = pet('kitkat','cat',1)
joey = pet('joey','rat',1)
print(p1.name,p1.pettype,p1.age)
print(p2.name,p2.pettype,p2.age)
print(joey.name,joey.pettype,joey.age) 
        