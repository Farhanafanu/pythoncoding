def factorial(num):
    if num>1:
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        return fact

res=factorial(5)
print(res)