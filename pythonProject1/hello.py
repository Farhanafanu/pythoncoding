from contry import america
# a=input("enter number")
# b=input("enter 2nd number")
#
#
# sum=int(a)+int(b)
# sum=int(a+b)
# print(" hi how are you"+str(a))
# print(a+d)
# print(sum)
# b=20
# c=30
# print(b,c)
# def sum(num):
#     currentsum=0
#     runsum=[]
#     for i in num:
#         currentsum+=i
#         runsum.append(currentsum)
#     return runsum
# num=[1,1,1,1,1-]
# result=sum(num)
# print(result)


def hello(func):
    def wrapper():
        print("hello")
        return func()
    return wrapper
@hello
def printhello():
    print("hai")


printhello()
