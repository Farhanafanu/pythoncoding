# str="haifriends"
# print(str)
# print(str[0:5])
# print(str[:6])
# print(str[5:])
# print(str[2:5])
# print(str[2:])
# print(str[2:5])
# print(str[:5])
# print(str[:-1])
# print(str[-5:-1])
# str="haiwelcome"
# print(str[1:-1])
# print(str[1:5])
# print(str[-3:-1])


str = "aaaabbbbcccc"
new=""
for char in str:
    if char not in new:
        new+=char


print(new)

new=new[::-1]
print(new)


