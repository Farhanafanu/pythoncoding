# def sentence(sent):
#     words=sent.split()
#     reverseword=words[::-1]
#     return " ".join(reverseword)
# sent="my name is farhana"
# res=sentence(sent)
# print(res)
# dict={"a":1,"b":2,"c":3,"d":4}
# values=dict.values()
# print(values)
# sum=0
# for value in values:
#     if value%2==1:
#         sum+=value
# print(sum)
# str="farhana"
# vowel="aeiou"
# count=0
# for i in  str:
#     if i in vowel:
#         count+=1
# print(count)


# input_str = "farhana"
# char_count = {}
#
# for char in input_str:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#
# for char, count in char_count.items():
#     print(f"Character '{char}' count: {count}")
str="farhana"
count=0
dup=" "
for char in str:
    if char not in dup:
        dup+=char

        count+=1
print(count)
