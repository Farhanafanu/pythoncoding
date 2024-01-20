list=[1,3,4,5]
e=3
list[0],list[-1]=list[-1],list[0]
print(list)
print(len(list))
print(max(list))
print(min(list))
rev=list[::-1]
print(rev)
for i in list:
    if e in list:
        print("present")
    else:
        print("not")