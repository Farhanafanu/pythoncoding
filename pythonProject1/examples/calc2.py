def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    max_length = 1  # Minimum length is 1 since each element is a valid subsequence
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length


# Example usage
nums = [1, 3, 5, 4, 7,8,9,10,2]
result = longest_increasing_subsequence(nums)
print(result)  # Output should be 3, as the longest increasing subsequence is [1, 3, 5]
