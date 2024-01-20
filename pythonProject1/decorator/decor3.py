def upper(fun):
    def wrapper(n):
        upper=fun(n)
        modifiedfun=upper.upper()
        return modifiedfun
    return wrapper
@upper
def name(n):
    return "hello"+n
print(name("fanu"))
