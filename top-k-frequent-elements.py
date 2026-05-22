# 2. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.
# Order does not matter.
# Input:
# nums = [1,1,1,2,2,3], k=2
# Output:
# [1,2]

nums = [1,1,1,2,2,3]
k=2

def top_k_frequent_elements(nums, k):
    elements_count = {}
    result = []
    max_freq=0
    max_key=None
    
    for i in range(len(nums)):
        if nums[i] in elements_count:
            elements_count[nums[i]] += 1
        else:
            elements_count[nums[i]] = 1

    for _ in range(k):
        max_freq=0
        max_key=None
        
        for key in elements_count:
            if elements_count[key] > max_freq:
                max_freq=elements_count[key]
                max_key=key
                
        result.append(max_key)           
        del elements_count[max_key]
    
    return result

print(top_k_frequent_elements(nums,k))