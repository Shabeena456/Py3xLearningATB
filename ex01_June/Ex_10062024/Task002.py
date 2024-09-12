# Q1. Develop a Python script that calculates the square and cube
# of a given number.num = 2 sq - 4, c = 8

num = float(input("Enter the number:"))
square=num**2
print("The square of",num,"is",square)
cube=num**3
print("The cube of", num, "is", cube)


print("-----------------------------------------------------")


def calculate_square_and_cube(number):

    square = number ** 2

    cube = number ** 3

    return square, cube



# Example usage

number = float(input("Enter a number: "))

square, cube = calculate_square_and_cube(number)

print(f"The square of {number} is {square}")

print(f"The cube of {number} is {cube}")

print("-----------------------------------------------------")

# Q2. Create a program that takes two numbers as input and prints whether
# the first number is greater than, less than, or equal to the second number.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The first number is greater than the second number.")
elif num1 < num2:
    print("The second number is greater than the first number.")
else:
    print("The first number is equal to the second number.")

print("-----------------------------------------------------")


def compare_numbers(num1, num2):

    if num1 > num2:

        return "The first number is greater than the second number."

    elif num1 < num2:

        return "The first number is less than the second number."

    else:

        return "The first number is equal to the second number."



# Example usage

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

result = compare_numbers(num1, num2)

print(result)


print("-----------------------------------------------------")
