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

# fib