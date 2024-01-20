list=[1,2,3,4,5,6,7,6,5,3]
dup=[]
for i in list:
    if i not in dup:
        dup.append(i)
print(dup)