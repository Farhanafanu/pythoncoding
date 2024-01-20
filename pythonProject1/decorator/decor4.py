# def hello(func):
#     def wrapper():
#         print("hello world")
#         return func
#     return wrapper
#
# @hello
# def printhello():
#     pass
# printhello()
# def add(func):
#     def wrapper(a,b):
#         return func(a,b)
#     return wrapper
# @add
# def addition(a,b):
#     return a+b
# res=addition(4,5)
# print(res)
def mul(func):
    def wrapper(a,b):
        return func(a,b)
    return wrapper
@mul
def multiple(a,b):
    return a*b
res=multiple(4,5)
print(res)