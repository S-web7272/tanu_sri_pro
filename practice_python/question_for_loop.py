#ques 1: wap to find those number which are divisible by 7 and multiple of 5,between 1500 and 2700

for  x in range(1500,2701):
    if (x%7 == 0)and (x%5 == 0):
        print(x)

#ques 2: wap to count the number of even and odd numbers from a series of number
numbers = (1,2,3,4,5,6,7,8,9)
count_odd =  0
count_even = 0
for a in numbers:
    if not a % 9:
        count_even+=1

    else:
        count_odd+=1

print("number of even numbers :",count_even)
print("number of odd numbers :",count_odd)

#ques 3: wap to get the fibonacci series between0 to 50.
x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y 

#ques 4: wap that accepts a word from the user and reverse it.

word = input("input a word to reverse: ")

for char in range(len(word) -1, -1, -1):
    print(word[char],end=" ")
print("\n")
