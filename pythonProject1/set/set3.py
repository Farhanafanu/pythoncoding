set1={1,2,3,4,5}
set2={6,7,8,9,10,4,1,2,3,5}
print(set1.intersection(set2))
# disjoint set
print(set1.issubset(set2))
set1.issuperset(set2)
print(set2.issuperset(set1))
print(set1.isdisjoint(set2))
del set2
print(set2)