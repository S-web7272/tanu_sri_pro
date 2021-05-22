# wap  to store all the armstrong numbers till 100000
for num in range(10,100000):
    pow = len(str(num))
    temp=num
    sum=0
    while num >0:
        digit = num % 10

        sum=sum+digit**pow
        num=num//10
        if temp==sum:
            print(temp,end=' ')