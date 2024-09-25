# Take the 2 integer from user and print the sum of those two numbers
# Type conversion is necessary.we have to str ->int
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = a+b
print(c)




# Take the 2 int number from the user and we want to add them.
# We need to use the input() function.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# type conversion - str -> int -> ? int()
result = int(num1)+int(num2)
print(result)

#  + ->  int  sum operation
#  + -> str - concat
# int to str -> str()
# str to int -> int()

print(type(int(num1)))

print(type(int(result)))
