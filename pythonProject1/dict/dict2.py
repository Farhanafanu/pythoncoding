phoneno={"aslam":8547557076,"farhana":9656145823}
# print(phoneno)
# print(phoneno["aslam"])
# #case sensitive,mutable
# phoneno["aslam"]=1234567890
# print(phoneno)
for i in phoneno:
    print(i)
    print(phoneno[i])

phoneno2=phoneno.copy()
print(phoneno2)
print(len(phoneno))