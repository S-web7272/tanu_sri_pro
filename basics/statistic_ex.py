# wap to display mean,max,min,sum,size

data =[5,7,9,3,9,2,1,98,567,34,23,98,45,87,45,34,90.67]

total = sum(data)
size = len(data)
mean = total/size
mx = max(data)
mn = min(data)

print('mean',mean)
print('max',mx)
print('min',mn)
print('sum',total)
print('size',size)