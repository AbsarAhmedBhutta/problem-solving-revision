# 6. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without duplicate characters.
# Input:
# "abcbabcb"
# Output:
# 3
# ("abc")

def longest_substring(s):
    left = 0
    seen = set()
    max_length = 0
    best_left=0
    
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
            
        seen.add(s[right])
        
        if right-left+1 > max_length:
            max_length = right-left+1
            best_left=left
    
    return max_length, s[best_left:best_left+max_length]

print(longest_substring("abbabcb"))