temp = {
    'name':'smita srivastava',
    'designation':'Assistant level 3',
    'salary':{
        'basic':32000,
        'ra':500000,
        'dr':8000,
        'yup':9000
    },
    'dept':'developers',
    'doj':{
        'year':4000,
        'month':7,
        'day':12
    },

}

print(temp)
print(temp['name'])
print(temp['salary']['dr'])
print(temp['dept'])
print(temp['doj']['year'])

stockprices = dict(google = 245,facebook = 27.44,crome =400.33)
print('another dictionary')
print(stockprices)

# add  a value
print('adding a value')

stockprices['pogo'] = 238.56
print(stockprices)

temp['phone'] = 123456
print(temp)

# update a value
print('updateing a value')

stockprices['facebook'] = 180.65
print(stockprices)

temp['dept'] = 'sales'
print(temp)