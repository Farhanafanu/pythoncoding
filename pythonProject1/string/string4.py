str1="good"
str2="morning"
str3=str1+str2
print(str3)
str4="the great day"
temp=""
rev=""
for i in str4:
    if i!=" ":
        temp=i+temp
    else:
        rev=rev+temp
        temp=""
print(rev)

