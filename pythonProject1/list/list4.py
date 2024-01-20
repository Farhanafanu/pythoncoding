# lampda function
list1=[1,2,3,4,5,6,7,8,9,10]
odd=[i**2 for i in list1 if i%2==1]
print(odd)
sum=0
for i in odd:
    sum=sum+i

print(sum)