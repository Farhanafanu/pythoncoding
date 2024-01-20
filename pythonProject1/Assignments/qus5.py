totalmark = float(input("Enter the mark: "))

if totalmark >= 90:
    print("A grade")
elif 80 <= totalmark <= 89:
    print("B grade")
elif 70 <= totalmark <= 79:
    print("C grade")
elif 60 <= totalmark <= 69:
    print("D grade")
elif 50 <= totalmark <= 59:
    print("E grade")
else:
    print("Failed")
