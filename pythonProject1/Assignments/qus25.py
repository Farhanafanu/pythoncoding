class MenuOptionException(Exception):
    pass
def menu():
    print("Menu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")

    choice = input("Enter your choice: ")

    if choice == '1':
        raise MenuOptionException("Option 1 is not allowed.")
    elif choice not in ('1', '2', '3'):
        raise ValueError("Invalid choice. Please enter a valid option.")

try:
    menu()
except MenuOptionException as e:
    print("Menu Option Exception:", e)
except ValueError as e:
    print("Value Error:", e)
except Exception as e:
    print("Other Exception:", e)
