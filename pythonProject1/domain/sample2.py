def fibinocci(num):
    a=0
    b=1
    if num==1:
        return 1
    else:
        print(a)
        print(b)
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c)

fibinocci(10)
