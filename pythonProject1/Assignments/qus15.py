def getArray(arr):
    size = int(input("Enter the size of the array: "))
    print("Enter elements for the array:")
    for i in range(size):
        element = int(input("Enter elements  "))
        arr.append(element)
def displayArray(arr):
    print("Array:", arr)
def main():


    array = []
    getArray(array)
    displayArray(array)

main()