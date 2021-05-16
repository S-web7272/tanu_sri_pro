x = [1,2,3,4,5]
colors = ['red','blue','black']
randomval = [22,33,44,55,66]

print('normal ->',x)
x.reverse()
print('reverse ->',x)
x.reverse()
print('back to normal ->',x)

print('normal ->',colors)
colors.reverse()
print('alphabetical sort ->',colors)

randomval.sort()
print('sorted',randomval)

randomval.sort(reverse=True)
print('sorted',randomval)

#count function work the same as string count
y = [1,2,3,4,5,6,7,8,9,3,5,7,8,6,4,2,8,5,9,3,5,2,9,5,3,2]
two_count = y.count(2)
three_count = y.count(3)
eight_count = y.count(8)

print('2 occurs ->',two_count)
print('3 occurs ->',three_count)
print('8 occurs ->',eight_count)
