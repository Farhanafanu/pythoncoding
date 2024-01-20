#used to store multiple elements,hetrogenious,not allowing duplicates,unorderd,indexing is not allowed,cant change values
set1={1,2,3,4,5,6,7,8,9,10,"hey",1,True}
print(set1)
#slicing and indexing is not allowed in set
set2={}
set1.add(99)
set1.add((13,14,15))
print(set1)
set1.remove(1)
set1.discard(3)
set1.discard(90)
print(set1)
set1.pop()
print(set1.pop())

set1.clear()
print(set1)
print(len(set1))
print(type(set2))
print(type(set1))