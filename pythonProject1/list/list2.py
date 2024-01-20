list1=[1,2,3,4,5,6,7,6]
dup=[]
for i in list1:
    if i not in dup:
        dup.append(i)
    else:
        print(i)