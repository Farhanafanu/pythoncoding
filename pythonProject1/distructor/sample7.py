# def changeword(sentence):
#     words=sentence.split()
#     newwords=[word.capitalize() for word in words]
#     return " ".join(newwords)
# sentence="my name is munna"
# res=changeword(sentence)
# print(res)
# def hello(func):
#     def wrapper():
#         print("hello world")
#         return func
#     return wrapper
# @hello
# def printhello():
#     pass
# printhello()
def add(func):
    def wrapper(a,b):
        return func(a,b)
    return wrapper
@add
def addition(a,b):
    return a+b
res=addition(4,5)
print(res)
