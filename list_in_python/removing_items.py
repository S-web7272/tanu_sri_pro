numbers = [1,2,3,4,5,6]
names = ['ravi','shiva','eshita','neha','ashi','ajay']
heights = ['ravi',5.6,'shiva',6,'eshita',5.1]
info = [True,True,False,True,False]
marks_per_year = [[45,67,45],[67,34,26],[78,56,34]]
teams =[['raja','rani','raju'],['jack','jamie'],['alex','alan']]
smileys = ['@','#','*']

print(numbers)
numbers.remove(5) #remove a value
print(numbers)

#numbers.remove(10) #error
marks_per_year[0].remove(45) #remove from sublist
print(marks_per_year)
names.remove('ajay')
print('removed ajay',names)
names.pop() #last value is removed by default
print('last value',names)
names.pop(1)
print('value at index 1',names)
marks_per_year.clear()
teams.clear()
print(marks_per_year)
print(teams)