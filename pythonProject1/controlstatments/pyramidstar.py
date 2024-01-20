
rows = int(input("Enter the number of rows for the pyramid: "))

i = 1
while i <= rows:

    spaces = rows - i
    while spaces > 0:
        print(" ", end="")
        spaces -= 1

    # Print stars
    stars = 1
    while stars <= i:
        print("* ", end="")
        stars += 1

    # Move to the next row
    print()
    i += 1
