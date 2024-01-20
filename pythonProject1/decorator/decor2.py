# def adddecor(func):
#     def wrapp(a, b):
#         result = func(a, b)
#         return result
#     return wrapp
#
# @adddecor
# def add(a, b):
#     return a + b
#
# print(add(5, 8))
def loancheck(func):
    def wrapper(name,salary):
        if salary<25000:
            raise Exception ("loan is not applicable")
        else:
            return func(name,salary)
    return wrapper
@loancheck
def eligiblity(name,salary):
    return "eligible"
res=eligiblity("aju",55000)
print(res)