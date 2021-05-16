names = ['smita srivastava','vaishali dixit','nidhi chaubey','divya srivastava',
        'vaibhav shrimali','harshit tripathi','rhidhi mishra']

names_containing_e = [name for name in names if 'e' in name]

names_capitalized = [name.title() for name in names]

names_ending_with_a = [name for name in names if name.endswith('a')]

print(names)
print(names_containing_e)
print(names_capitalized)
print(names_ending_with_a)
