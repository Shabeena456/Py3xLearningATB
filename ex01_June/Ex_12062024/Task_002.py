#
#
# A leap year is divisible by 4,
# but not by 100 unless it is also divisible by 400.
#
# Use an if-else statement to make this determination.

# (year % 4 == 0)
# (year % 100 != 0)
# (year % 400 == 0)

year = int(input("Enter the year:\n"))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a Leap Year")
else:
    print("This is Not Leap Year")

print("=================================================")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
       return ("Leap year")
    else:
        return ("not leap year")

year = int(input("Enter the year:\n"))

result =is_leap_year(year)
print(result)

print("=================================================")

# # Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal),
# # isosceles (exactly two sides are equal), or scalene (no sides are equal).

side1 = float(input("Enter side 1:\n"))
side2 = float(input("Enter side 2:\n"))
side3 = float(input("Enter side 3:\n"))

if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles")
else:
    print("Scalene")


print("=================================================")

    # # Task - Fibonacci series and Factorial

# Factorial
import math
import math


result = math.factorial(5)
print(result)

print("=================================================")


n = 4
factorial = 1

# range(1,10) #1-9

while n > 0:
    factorial = factorial * n
    n = n - 1
print(factorial)

print("=================================================")
for i in range(1, n + 1):
   factorial= factorial * i

print(factorial)

