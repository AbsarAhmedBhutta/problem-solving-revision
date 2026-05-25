# 8. Minimum Window Substring
# Given strings s and t, return the smallest substring of s containing all characters of t.
# Input:
# s="ADOBECODEBANC"
# t="ABC"
# Output:
# "BANC"

def min_window_substring(s, t):
    left = 0
    valid_substring_dict = {"substring": []}
    substring = ''
    valid = False
    
    for right in range(len(s)):
        print(right)
        while valid is True:
            left += 1
            
        if all(char in substring for char in t):
            print("VALID")
            valid_substring_dict["substring"].append(substring)
            valid=True
        else:
            valid=False
                    
        substring += s[right]
    
    return valid_substring_dict

print(min_window_substring("ADOBECODEBANC", "ABC"))