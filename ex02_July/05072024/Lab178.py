import os


file_name= os.open('testdata.txt',os.O_RDONLY)
os.write(file_name,b'Hello I am writing')
os.close(file_name)

