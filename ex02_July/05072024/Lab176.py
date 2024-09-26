# Standard lib Python Whihc Can help

# # How do you List all the directories

import os
all_dir = os.listdir(r"C:\Users\Asus\PycharmProjects\Py3xLearningATB\ex02_July\05072024")
print(all_dir)





# Epoch time to Normal time

# Environment Variables
# env variables are those which are present in your command line anyway.
# JDK, Variable

# Set an environment variable
os.environ['MY_VAR'] = 'lucky'
print(os.getenv("MY_VAR"))