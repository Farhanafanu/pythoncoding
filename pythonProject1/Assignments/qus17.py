class Calculator:
    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
calculator = Calculator()
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1/2/3/4): "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if choice == 1:
    result = calculator.addition(num1, num2)
elif choice == 2:
    result = calculator.subtraction(num1, num2)
elif choice == 3:
    result = calculator.multiplication(num1, num2)
elif choice == 4:
    result = calculator.division(num1, num2)
else:
    print("Invalid choice!")

print("Result:", result)

