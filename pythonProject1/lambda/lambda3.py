number=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,number))
odd=list(filter(lambda x:x%2==1,number))
print(number)
print(even)
print(odd)