def hello_decorator(func):
    def wrapper():
        print("HELLO WORLD")
        return func()
    return wrapper

@hello_decorator
def empty_function():
    pass

empty_function()


