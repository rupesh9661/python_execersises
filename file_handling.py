import os
file=open("files/demo.txt", 'w')
file.write("this is dummy file created using python file handling ")
file.close()

file2= open("files/demo.txt", 'r')
print(file2.read())
# os.remove("files/demo.txt")