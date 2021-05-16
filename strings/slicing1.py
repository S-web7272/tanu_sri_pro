name = 'vijay Deenanath chauhan'

fname = name[0:5] #vijay
print(fname)
mname = name[6:-8] #deenanath
print(mname)
lname = name[-7:len(name)]
print(lname)

# better version of fname and lname slices
fname = name[:5] 
lname = name[-7:]
print(fname,lname)

#fullname
print(name[:])

#reverse the name
print(name[::-1])

#every 2 second char in string
print(name[::2])