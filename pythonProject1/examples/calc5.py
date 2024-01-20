list=["apple",'grape',"banana"]
list.sort()
print(list)
list.reverse()
print(list)
list2=[]
for i in list:
    if "apple" in list:
     list2.append(i)
     print(list2)
list3=[]
list3=list.copy()
print(list3)