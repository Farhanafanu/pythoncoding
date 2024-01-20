
def binarysearch():
    list=[1,2,3,4,5,6,7,8,9,10]
    list.sort()
    print(list)
    flag=0
    element=int(input("enter element to find"))
    lower=0
    upper=len(list)-1
    while (lower<=upper):
        mid=(lower+upper)//2
        if element>list[mid]:
            lower=mid+1
        elif element<list[mid]:
            upper=mid-1
        elif element==list[mid]:
            flag=1
            break
    if flag==1:
        print("element found ")
    else:
        print("eleemnt not found")
binarysearch()