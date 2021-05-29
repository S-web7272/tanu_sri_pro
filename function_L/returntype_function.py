def mean(*numbers):
    if numbers:
        return sum(numbers)/len(numbers)


n1 = mean(1,2,3,4,5)

print(mean(1,2,3,4,5,5,6))

n2 = n1 * 10 
print('meanx10',n2)

def word_counter(sentence):
    if sentence:
        words = sentence.split()
        count = len(words)
        return count

from string import punctuation

def clean_punc(sentence):
    for char in punctuation:
        sentence = sentence.replace(char,'')
    return sentence

c1 = word_counter(' ')
c2 = word_counter('hello guys,what are you doing here and where are you going on')

s = 'hello guys,what are you doing here and where are you going on'
clean_s = clean_punc(s)
count = word_counter(clean_s)
print(s)
print(clean_s)
print(count)

c = word_counter(clean_punc(s))

