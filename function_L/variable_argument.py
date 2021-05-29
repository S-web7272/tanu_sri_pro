print('tanya','tanvi','tivi','tanu',sep='$$$')

def mean(*numbers):
    if numbers:
        tot = sum(numbers)
        print("mean=>",sum(numbers)/len(numbers))


mean()
mean(1)
mean(23,54,67,45)
mean(7,5,9,4,3,5,2,9,7,5,4,7,9,1,2,3,5,6,3,8,4,7,566)

def aggr(*numbers, operation = 'sum'):
    if numbers:
        if operation == 'sum':
            print('total',sum(numbers))
        elif operation == 'mean':
            print('mean',sum(numbers)/len(numbers))
        elif operation == 'max':
            print('max',max(numbers))


aggr(23,67,45,34,78,45,34,678)
aggr(12,45,56,34,76,operation= 'mean')
aggr(34,67,345,3,67,78,556,34,34,45,34,67,45,8,55,45,operation='max')
aggr(34,67,345,3,67,78,556,34,34,45,34,67,45,8,55,45,operation='sum')

# **variablename -> variable number of keyword arguments (**kwargs)

def function(**info):
    for k,v in info.items():
        print(k,v)

function(color='red',x=28,y=39,size=(100,100))
function(font='calibri',fontsize=20,rotation=100)