
# def sentance(sent):
#     result=" "
#     count=0
#     for char in sent:
#         if count%2==0:
#             result+=char
#         else:
#             result+=char.upper()
#         count+=1
#     return result
# sent=" my name is farhana"
# res=sentance(sent)
# print(res)
# def sentence(sent):
#     words=sent.split()
#     reversed=words[::-1]
#     return " ".join(reversed)
#
# sent="my name is farhana"
# res=sentence(sent)
# print(res)
# sent="my name is farhana"
# words=sent.split()
# print(words)
# print(max(len(word) for word in words))


# list=[1,2,3,2,1]
# count=0
# dup=[]
# for i in list:
#     if i not in dup:
#
#         count+=1
#     else:
#         count=1
#     print
# my_list = [1, 2, 3, 2, 1]
# count_dict = {}
# for i in my_list:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
#
# for key, value in count_dict.items():
#     print(f"Element {key} occurs {value} times.")
#
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverse_dict = {value: key for key, value in original_dict.items()}
print(inverse_dict)

