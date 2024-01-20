# try:
#     # Code that may raise an exception
#     # ...
# except SomeException as e:
#     # Code to handle the exception
#     # ...
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
