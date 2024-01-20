size=int(input("enter array size"))
array=[]
array1=[]
for i in range(size):
    element=int(input("enter elements"))
    array.append(element)
array1=array[:]
print("array",array)
print("copied arrar",array1)
element1=int(input("enter elemnt"))
array1.append(element1)
print(array1)
array, array1 = array1, array
print("after swapping:")
print("first array")
print(array)
print("copied array")
print(array1)