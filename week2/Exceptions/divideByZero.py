# This should trigger an exception
# print(str(5/0))
# ZeroDivisionError
# Traceback (most recent call last):
#   File "divideByZero.py", line 2, in <module>
#     print(str(5/0))
# ZeroDivisionError: division by zero

# So we use Try-Catch
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

import random

for i in range(0, 20):
    try:
        result = random.randint(0, 10) / random.randint(0, 10)
    except ZeroDivisionError:
        print("Cannot divide by 0!")
    else:
        print(result)
