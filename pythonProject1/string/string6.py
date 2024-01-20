text = "Python is awesome!"

# Changing case
print(text.lower())  # Output: "python is awesome!"
print(text.upper())  # Output: "PYTHON IS AWESOME!"

# Finding substrings
print(text.startswith("Python"))  # Output: True
print(text.endswith("awesome!"))  # Output: True
print(text.find("is"))  # Output: 7

# Replacing characters
print(text.replace("awesome", "amazing"))  # Output: "Python is amazing!"

# Splitting strings
words = text.split()  # Output: ['Python', 'is', 'awesome!']
