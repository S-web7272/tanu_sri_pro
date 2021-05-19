msg = 'Most of us wonder if there is a God and if He really is the God of the Bible.'
#ques 1 remove all vowels from a string
a = ['a','e','i','o','u']
for c in msg:
    if c in a:
        msg = msg.replace(c,'')

#ques 2 count all vowels in a string
l = 0
for c in msg:
    if c in a:
        l+=1
print('no of vowels in string is -->',l)
print(msg)