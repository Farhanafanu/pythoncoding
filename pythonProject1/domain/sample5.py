a=input("enter the string")
length=len(a)
flag=0
for i in range(length):
    if a[i]!=a[length-i-1]:
        flag=1
        break
if flag==0:
    print("palium")
else:
    print("not palium")