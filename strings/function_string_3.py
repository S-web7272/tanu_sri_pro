# find and index are exactly same , but find is  used because it gives no error
msg = 'Most of us wonder if there is a God and if He really is the God of the Bible'

author_idx = msg.find('author')
print('author word starts at',author_idx)

# the normal version
and_idx = msg.find('and')
print('and occurs at index',and_idx)

# with a tricky hack 
and_idx = msg.find('and ')
print('and occurs at index',and_idx)

# with a start position
and_idx = msg.find('and',10)
print('and occurs at index',and_idx)

#reverse find
and_idx = msg.rfind('and')
print('and occurs at index',and_idx)

#index example
and_idx = msg.index('and')
print('and occurs at index',and_idx)

#find ex where string is not found => -1
writer_idx = msg.find('writer')
print('writer occurs at index',writer_idx)