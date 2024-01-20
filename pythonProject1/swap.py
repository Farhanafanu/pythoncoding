# a=int(input("enter the number1"))
# b=int(input("enter 2nd number"))
# print(type(a),type(b))
# # temp=a
# # a=b
# # b=temp
# a,b=b,a
# print(a,b)
# #swapping
# """ff,dvfk"""
# s="hi friends"
# print(len(s))
# print(s[5])
# print(s[4:7])
# print(s[-1])
# def chocolate(sum):
#     my_list = [1,2,2]
#     min_val = float('inf')
#     second_min = float('inf')
#
#     for num in my_list:
#         if num < min_val:
#             second_min = min_val
#             min_val = num
#         elif num < second_min and num != min_val:
#             second_min = num
#
#     print("The minimum value is:", min_val)
#     print("The second minimum value is:", second_min)
#     s=sum-(min_val+second_min)
#     if s>=0 :
#         return s
#     else:
#         return sum
#
# result = chocolate(3)
# print("Result:", result)
a=10
b=5
print(a,b)
a,b=b,a
print(a,b)
