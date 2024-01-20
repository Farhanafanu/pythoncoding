rows = 4
number = 7

for i in range(rows, 0, -1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()
    number -= i * 2 - 1

