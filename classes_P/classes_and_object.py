
# simple classes

class foodItems:
    pass

# properties and behaviar
class dog:
    breed = 'parsian'

class product:
    # method -> class method -> used directly with class
    def help():
        print('this is class under contruction')

####creation object####
#object = classname()

maggi = foodItems()
roti = foodItems()
name = 'tanu'

print(type(name))
print(type(maggi))

minnu = dog()
lilly = dog()

print(minnu,lilly)
print(minnu.breed)
print(lilly.breed)

keyboard = product()
monitor = product()

#class function
product.help()

# should not be used by object
#keyboard.help()