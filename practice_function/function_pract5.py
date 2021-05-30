# write a function to find factorial of a number but also store the factorial calculated in a dictionary as done in the fibonacci series:

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact = fact * num
    return(fact)

factorial(7)
