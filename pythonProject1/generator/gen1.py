# def gen():
#     yield 10
#     yield 20
#     yield 30
#     yield 40
# x=gen()
# value=next(x)
# # value=next(x)
# # value=next(x)
# # value=next(x)
# print(value)
def gen():
    yield 50

x=gen()
result=next(x)
print(result)
