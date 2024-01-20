# str="malayala"
# str2=str[::-1]
# if str==str2:
#     print("palium")
# else:
#     print("not")
# str="malayala"
# rev=str[::-1]
# print(rev)
# str = "malayalam"
# str = str.replace("m", " ",1)
# print(str)
# input_str = "malayalam is a powerful object"
# words = input_str.split()
#
# for word in words:
#     if len(word) % 2 == 0:  # Check if the length of the word is even
#         print(word)
# str = "malayalm is powerful"
# half_length = len(str) // 2
#
# for i in range(half_length):
#     str = str.upper()  # Assign the uppercased version back to 'str'
#     print(str)
# str = "my name is farhana"
# words = str.split()
#
# for i, word in enumerate(words):
#     if len(word) < 1:
#         words[i] = word.upper()
#     elif len(word) < len(words[-1]):
#         words[i] = word.upper()
#
# for word in words:
#     print(word)
# str="farhanaio"
# vowels="aeiou"
# for i in str:
#     if i in vowels:
#         print(i)
# str="farhanafar"
# count={}
# for i in str:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
#
# for key,value in count.items():
#     print(key,value)
#
str="farhana is good girl"
word=str.split()

result=" ".join(word)
print(result)