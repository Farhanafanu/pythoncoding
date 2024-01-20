def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def multiply(a, b):
    return a * b

# Calling decorated functions
print(add(2, 3))       # Output: Calling function: add
                       #         Function add finished
                       #         5
print(multiply(3, 4))  # Output: Calling function: multiply
                       #         Function multiply finished
                       #         12
