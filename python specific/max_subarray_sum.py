# 7. Maximum Sum Subarray of Size K
# Given an array and integer k, find the maximum sum of any contiguous subarray of size k.
# Input:
# [2,1,5,1,3,2], k=3
# Output:
# 9

def longest_subarray_sum(input, k):
    n = len(input)
    window_sum=sum(input[:k])
    max_sum = window_sum
    
    for i in range(k, n):
        window_sum += input[i] - input[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum

input=[2,1,5,1,3,2]
k=3

print(longest_subarray_sum(input,k))