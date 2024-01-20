def oddevn(num):
    if num%2==0:
        return "even"
    else:
        return "odd"


num=int(input("enter the number"))
result=oddevn(num)
print(result)
num=int(input("enter the number"))
oddevn=lambda num:"even"if num%2==0 else "odd"
result=oddevn(num)
print(result)