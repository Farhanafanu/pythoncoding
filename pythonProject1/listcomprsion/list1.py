#new_list = [expression for item in iterable if condition]
squre=[i**2  for i in range(1,6) if i%2==0 ]
sum=0
for i in range(len(squre)):
    sum=sum+i
    i=i+1
print(sum)
print(squre)
cube=[i**3 for i in range(1,6)]
print(cube)
num=[1,2,3,4,5,6,7,8,9,10]
evn=[i for i in num if i%2==0]
print(evn)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(result)  # Output: ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
