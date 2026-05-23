# 4. Contains Duplicate
# Given an integer array nums, return True if any value appears at least twice.
# Otherwise return False.
# Input:
# [1,2,3,1]
# Output:
# True

def contains_duplicate(nums):
    seen=[]
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        else:
            seen.append(nums[i])
        
    return False
        
nums = [1,2,3,1]
print(contains_duplicate(nums))