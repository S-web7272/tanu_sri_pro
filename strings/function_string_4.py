# replace is usefull to replace data with something else in strings
msg = 'Most of us wonder if there is a God and if He really is the God of the Bible.'

umsg = msg.replace('author','writer')
print(umsg)

amsg = msg.replace('and','or')
print(amsg)

#remove something
fmsg = msg.replace('God','')
print(fmsg)
