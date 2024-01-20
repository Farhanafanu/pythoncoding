size = int(input("Enter the size of the array: "))
array = []
for i in range(size):
    element = int(input("enter elements"))
    array.append(element)
for i in range(size - 1):
    max_index = i
    for j in range(i + 1, size):
        if array[j] > array[max_index]:
            max_index = j
    array[i], array[max_index] = array[max_index], array[i]
print("Sorted Array Descending Order:", array)
