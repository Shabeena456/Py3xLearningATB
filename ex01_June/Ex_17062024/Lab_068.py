
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

leap_or_not=is_leap_year(year)
print(leap_or_not)

print("=================================================")
