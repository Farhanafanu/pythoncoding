try:
    a=10/0
    print(a)
except ZeroDivisionError:
    print("can't divide by zero")
print("program complete")