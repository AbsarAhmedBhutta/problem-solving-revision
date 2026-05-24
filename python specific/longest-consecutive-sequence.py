# 5. Longest Consecutive Sequence
# Given an unsorted array, find the length of the longest consecutive sequence.
# Must run in O(n).
# Input:
# [100,4,200,1,3,2]
# Output:
# 4
# (1,2,3,4)
def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    print(nums_set)
    
    max_length = 0
    longest_sequence = []

    for i in nums_set:
        # start of sequence
        if i - 1 not in nums_set:
            print(i)
            current = i
            current_sequence = [current]

            while current + 1 in nums_set:
                current += 1
                current_sequence.append(current)

            if len(current_sequence) > max_length:
                max_length = len(current_sequence)
                longest_sequence = current_sequence

    return max_length, longest_sequence


nums = [100,101,4,200,1,3,2]

length, sequence = longest_consecutive_sequence(nums)

print(length)
print(sequence)