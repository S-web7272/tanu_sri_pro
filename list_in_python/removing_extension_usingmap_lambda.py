files = ['demo1.png','help,exe','demo2.png','read.doc']
print(files)

#normal version
cl_files = []
for file in files:
    name = file.split('.')[0]
    cl_files.append(name)

print(cl_files)

#lambda expresion

remove_ext = lambda filename: filename.split('.')[0]
clean_names = list(map(remove_ext,files))

print(clean_names)
