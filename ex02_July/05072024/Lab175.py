# OS Module
# OS module use to interact with the Operating system
#  get working dir, change dir, file exist , fileName, size file, Envir
import os
import math

print(os.name) # # e.g., 'posix' for Unix/Linux - Mac
# nt - windows

print(os.getcwd()) #it prints which current directory we are working on
# print(math.pi)

# os.chdir("C:\Users\Asus\PycharmProjects\Py3xLearningATB\ex02_July/")
# print(os.getcwd())

# print(os.listdir("C:\Users\Asus\PycharmProjects\Py3xLearningATB\ex02_July/"))
# os.mkdir("Lucky") #to make dir

# If you want to Read file, You want check if exist or not.

size = os.path.getsize('testdata.txt')
print(size)

if size != 0:
    print("File EXIST and has content")
else:
    print("File don't Exist, No Content")

# Get file modification time
mtime = os.path.getmtime('testdata.txt') #to get the modified time, that when this file is modified
print(mtime)

import time
print(time.gmtime(mtime))

print(time.localtime())
