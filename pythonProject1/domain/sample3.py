list=[1,2,3,4,5,6,7,8,9,10]
def linearsearch(list):
    e=int(input("enter the element"))
    flag=0
    for i in list:
        if i==e:
            flag=1
            break
    if flag==1:
        print("element found")
    else:
        print("not found")
linearsearch(list)


