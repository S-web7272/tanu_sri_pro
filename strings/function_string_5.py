#split and join
msg = 'Most of us wonder if there is a God and if He really is the God of the Bible.'
msg2 = 'i was eating food. the food is cold. then i lived happily ever after'

words = msg.split()
print(words)
print(len(words))

#decide the character or sub str to split from
words2 = msg2.split('.')
print(words2)
print(len(words))

#decide number of maxsplits
msg = "apple,banana,pasta,cheese,butter,mango"
words = msg.split(',',3)
print(words)

#decide number of maxsplits in reverse order
msg = "apple,banana,pasta,cheese,butter,mango"
words = msg.rsplit(',',3)
print(words)
