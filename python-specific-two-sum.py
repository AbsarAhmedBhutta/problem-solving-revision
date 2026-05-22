# Here are proper interview-style problem statements for all 20.
# 1. Two Sum
# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume exactly one solution exists.
# Input:
# nums = [2,7,11,15], target = 9
# Output:
# [0,1]
nums = [2,7,11,15]
target = 9

def two_Sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []
            

print(two_Sum(nums,target)) # O(N^2)

# above is O(N^2) making in O(N) below

def two_sum_optimal(nums, target):
    seen = {}
    
    for i in range(len(nums)):
        needed = target - nums[i]
        
        if needed in seen:
            return [seen[needed], nums[i]]
        
        seen[nums[i]]
    
    return []

print(two_Sum(nums,target)) # O(N)
