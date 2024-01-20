def replace_substring(input_string, old_substring, new_substring):
    modified_string = input_string.replace(old_substring, new_substring)
    return modified_string

# Example string
original_string = "I like apples, and I like bananas too."

# Substrings to replace
old_substring = "like"
new_substring = "enjoy"

# Replace the old substring with the new substring
result = replace_substring(original_string, old_substring, new_substring)
print(result)
