# 3. Product of Array Except Self
# Given an integer array nums, return an array where each position contains the product of all elements except itself.
# Do not use division.
# Input:
# [1,2,3,4]
# Output:
# [24,12,8,6]


def product_of_each_except_self(nums):
    result_nums = []
    
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i!=j:
                product*=nums[j]
        
        result_nums.append(product)   
    
    return result_nums

nums= [1,2,3,4]
print(product_of_each_except_self(nums))

# O(N)
