# Q1. Explain the difference between the = operator and the == operator in Python.

# = Operator (Assignment Operator):
# The = operator is used to assign a value to a variable.
# Example:
x = 5
y = "Hello"


# == Operator (Equality Operator):

# The == operator is used to compare two values for equality.
# It produces a Boolean value (True or False) based on whether the values being compared are equal.
# Example:

a = 5
b = 5
c = 10
print(a == b)  # This will print: True
print(a == c)  # This will print: False

# Q2. What does the ** operator do in Python, and how is it used?
# The ** operator is used to raise a number to the power of another number.

result = 2 ** 3
print(result)  # This will print: 8

# Q3. What does the ^ operator do in Python, and in what context is it commonly used?
# the ^ operator is the bitwise XOR (exclusive OR) operator.
# It is used to perform a bitwise XOR operation between two integers.
# The XOR operation compares each bit of the integers and
# returns 1 if the bits are different, and 0 if they are the same.


# Syntax: a ^ b


a = 5  # In binary: 0101
b = 3  # In binary: 0011
result = a ^ b
print(result)  # This will print: 6 (In binary: 0110)
