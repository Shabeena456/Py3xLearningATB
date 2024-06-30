# Multiple Conditions
# Switch in JAVA - I
# Match Case
# numbers = int(input("Enter a Number\n"))
# browser = str(input("Enter the browser name\n"))
# browser = browser.lower()
# match browser:
#     case "chrome":
#         print("Chrome code executed!")
#     case "firefox":
#         print("FF code executed!")
#     case _:
#         print("No browser Found!")

numbers = int(input("Enter a Number\n"))
# 3.10
match numbers:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case 6:
        print("You have entered 6")
    case _:
        print("No idea")


#         def allowed_to_attend_python_class(name):
#
# match name:
#
#     case "DELL":
#
#         print("Dell is allowed")
#
#     case "Shubham":
#
#         print("Shubham is allowed")
#
#     case "Pallavi":
#
#         print("Pallavi is allowed")
#
#     case _:
#
#         print("Not Allowed")
#
# allowed_to_attend_python_class("Shubham")
