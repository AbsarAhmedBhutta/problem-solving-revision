# Find all unique triplets whose sum equals zero.
# Input:
# [-1,0,1,2,-1,-4]
# Output:
# [[-1,-1,2],[-1,0,1]]

def all_unique_triplets(nums):
    n = len(nums)
    triplets = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))

    return [list(t) for t in triplets]


nums = [-1,0,1,2,-1,-4]
print(all_unique_triplets(nums))