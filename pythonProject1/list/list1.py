list1=[1,3,2,4,5,6,7,8,9,10]
list2=["hello",1,2,"hey"]

# multiple data can be store,ordered ,mutable.,hetrogenous
print(list2)
print(list2[1])
list1.append(33)
print(list1)
print(max(list1))
print(min(list1))
print(len(list1))
print(list2[-1])
#list slicing
print(list2[0:4])
print(list2[:])
print(list2[1:3])
print(list1[0:11:2])
# last 2 is skipping the 2 values
list1.sort()
print(list1)
list2.reverse()
print(list2)
list2.remove(2)
print(list2)
list2.insert(1,10)
print(list2)
list2.extend([1,23,45,6])
print(list2)
list2[1]=50
print(list2)
list2.pop()
print(list2)
list2.pop(2)
print(list2)