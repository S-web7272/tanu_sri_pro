num = []
print("enter the 10 values below, one value at a time")
for i in range(1,11):
    val = int(input(f'enter {i} >>'))
    num.append(val)

print('lenth of list',len(num))
print('sum of list',sum(num))
print('mean of list',sum(num)/len(num))
print('max of list',max(num))
print('min of list',min(num))




