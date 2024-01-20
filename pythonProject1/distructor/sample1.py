# class MyObject:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is created.")
#
#     def __del__(self):
#         print(f"{self.name} is being destroyed.")
#
#
# obj1 = MyObject("Object 1")
# obj2 = MyObject("Object 2")
#
#
# del obj1
from add import sample
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num= 10
res=fibonacci(num)

print("Fibonacci sequence:",res )
