class ArrayAddition:
    def getArray(self, arr):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print("Enter elements for the array:")
        for i in range(rows):
            row = []
            for j in range(cols):
                element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
                row.append(element)
            arr.append(row)

    def addArray(self, arr1, arr2):
        result = []
        rows = len(arr1)
        cols = len(arr1[0])
        for i in range(rows):
            row = []
            for j in range(cols):
                sum_element = arr1[i][j] + arr2[i][j]
                row.append(sum_element)
            result.append(row)
        return result

    def displayArray(self, arr):
        print("Array:")
        for row in arr:
            print(row)

array_addition = ArrayAddition()

array1 = []
array2 = []

array_addition.getArray(array1)
array_addition.getArray(array2)

sum_array = array_addition.addArray(array1, array2)

array_addition.displayArray(sum_array)
