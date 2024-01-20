def prime(num):
    if num<2:
        return "not prime"
    else:
        flag=0
        for i in range(2,num):
            if num%i==0:
                flag=1
                break

        if flag==0:
            return "prime"
        else:
            return "not prime"
num=int(input("enter number"))
res=prime(num)
print(res)
