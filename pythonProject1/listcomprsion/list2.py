list1=[1,2,3,4,5,-8]
list2=[4,5,6]
dup=[i for i in list1 if i in list2]
print(dup)
env=[i for i in list1 if i%2==0]
print(env)
odd=[i for i in list1 if i%2==1]
print(odd)
cube=[i**3 for i in list1 ]
print(cube)
squre=[i**2 for i in list1]
print(squre)
sum=0;
for i in squre:
    sum=sum+i
print(sum)
negt=[i for i in list1 if i<0]
print(negt)