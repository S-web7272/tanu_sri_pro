def remove_punc(sentence,punchuation='#$%@@%$()_+()'):
    for item in punchuation:
        if item in sentence:
            sentence = sentence.replace(item,' ')
        print(sentence)

msg = "hello guys,($^@$$^$^$)(^$^$%$@#$Z%@#$) i m shri"

remove_punc(msg,'()#$$$^:')
remove_punc(msg)

def summer(a,b,c=0,d=0):
    print(a + b + c + d)

summer(23,55)
summer(76,45,98)
summer(23,676,87,56)
summer(56,45,12,87)
summer(a=1,b=2,c=3,d=4)
