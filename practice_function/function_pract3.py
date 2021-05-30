# Write a function to tell user if he/she is able to vote or not(consider minimum age of  voting to be 18) 
def person_vote(age):
    age = int(input("Enter Age : "))
    if age>=18:
        print("Eligible")
    else:
        print("Not Eligible")

person_vote()
person_vote()