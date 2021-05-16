numbers = [1,2,3,4,5,6]
names = ['ravi','shiva','eshita','neha','ashi','ajay']
heights = ['ravi',5.6,'shiva',6,'eshita',5.1]
info = [True,True,False,True,False]
marks_per_year = [[45,67,45],[67,34,26],[78,56,34]]
teams =[['raja','rani','raju'],['jack','jamie'],['alex','alan']]
smileys = ['@','#','*']
primes = [2,3,5,7,11,13,17,19,23]

#indexing
x = numbers[0]
print(x)
winner = names[3]
print(winner)
print(heights[-1])
print(heights[-2])
print(marks_per_year[1])
print(marks_per_year[1][1])
print(marks_per_year[1][2])
print(marks_per_year[-1][-1])
extra_member = teams[0][-1]
print(extra_member)

# slicing
first_two_numbers = numbers[:2]
last_two_numbers = numbers[-2:] #last two
first_3_names = names[:3]
even_idx_names = names[::2]
print(first_two_numbers)
print(last_two_numbers)
print(first_3_names)
print(even_idx_names)
print(primes[::-1])
first_yr_2_subject_marks = marks_per_year[0][:2]
last_yr_2_subject_marks = marks_per_year[-1][-2]
print(first_yr_2_subject_marks)
print(last_yr_2_subject_marks)