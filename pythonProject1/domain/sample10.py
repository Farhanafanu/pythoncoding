def evnsums(nums):
    sum=0
    for i in nums:
        if i%2==0:
            sum+=i
    return sum
nums=[1,2,3,4,5]
res=evnsums(nums)
print(res)