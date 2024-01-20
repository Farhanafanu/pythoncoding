# word=input("enter the word")
# if word==word[::-1]:
#     print("paliundrom")
# else:
#     print("not paliundrome")
word= input("Enter a string: ")
length = len(word)
is_palindrome = True
for i in range(length):
    if word[i] != word[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
