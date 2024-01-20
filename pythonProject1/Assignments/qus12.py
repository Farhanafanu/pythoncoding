rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
array1 = []
array2 = []
print("Enter elements for Array 1:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i+1}, {j+1}) in array 1: "))
        row.append(element)
    array1.append(row)
print("Enter elements for Array 2:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i+1}, {j+1}) in array 2: "))
        row.append(element)
    array2.append(row)
sum_array = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(array1[i][j] + array2[i][j])

    sum_array.append(row)
print("Array 1:")
for row in array1:
    print(row)
print("Array 2:")
for row in array2:
    print(row)
print("Sum Array:")
for row in sum_array:
    print(row)
