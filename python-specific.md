Here are proper interview-style problem statements for all 20.
1. Two Sum
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
You may assume exactly one solution exists.
Input:
nums = [2,7,11,15], target = 9
Output:
[0,1]
2. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements.
Order does not matter.
Input:
nums = [1,1,1,2,2,3], k=2
Output:
[1,2]
3. Product of Array Except Self
Given an integer array nums, return an array where each position contains the product of all elements except itself.
Do not use division.
Input:
[1,2,3,4]
Output:
[24,12,8,6]
4. Contains Duplicate
Given an integer array nums, return True if any value appears at least twice.
Otherwise return False.
Input:
[1,2,3,1]
Output:
True
5. Longest Consecutive Sequence
Given an unsorted array, find the length of the longest consecutive sequence.
Must run in O(n).
Input:
[100,4,200,1,3,2]
Output:
4
(1,2,3,4)
6. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
Input:
"abcabcbb"
Output:
3
("abc")
7. Maximum Sum Subarray of Size K
Given an array and integer k, find the maximum sum of any contiguous subarray of size k.
Input:
[2,1,5,1,3,2], k=3
Output:
9
8. Minimum Window Substring
Given strings s and t, return the smallest substring of s containing all characters of t.
Input:
s="ADOBECODEBANC"
t="ABC"
Output:
"BANC"
9. Move Zeroes
Move all zeros to the end while maintaining relative order.
Do in-place.
Input:
[0,1,0,3,12]
Output:
[1,3,12,0,0]
10. Container With Most Water
Given heights, find two lines that hold maximum water.
Input:
[1,8,6,2,5,4,8,3,7]
Output:
49
11. 3 Sum
Find all unique triplets whose sum equals zero.
Input:
[-1,0,1,2,-1,-4]
Output:
[[-1,-1,2],[-1,0,1]]
12. Valid Anagram
Check whether two strings are anagrams.
Input:
s="listen"
t="silent"
Output:
True
13. Group Anagrams
Group words that are anagrams.
Input:
["eat","tea","tan","ate","nat","bat"]
Output:
[ ["eat","tea","ate"],
["tan","nat"],
["bat"]
]
14. Reverse Words in String
Reverse order of words.
Input:
"the sky is blue"
Output:
"blue is sky the"
15. Reverse Linked List
Reverse a singly linked list.
Input:
1 → 2 → 3 → 4
Output:
4 → 3 → 2 → 1
16. Detect Cycle in Linked List
Return True if linked list contains cycle.
Input:
1 → 2 → 3
↑     ↓
Output:
True
17. Valid Parentheses
Determine if brackets are valid.
Input:
"{[]}"
Output:
True
18. Daily Temperatures
For each day, find how many days until warmer temperature.
Input:
[73,74,75,71,69,72,76,73]
Output:
[1,1,4,2,1,1,0,0]
19. Binary Tree Level Order Traversal
Return values level by level.
Input:

3
  / \
 9  20
   / \
 15  7
Output:

[[3],[9,20],[15,7]]
20. Lowest Common Ancestor (BST)
Find lowest shared parent node.
Input:

6
     / \
    2   8
   / \
  0   4
Nodes: 2 and 4
Output:
2
This set alone covers around 70–80% of coding rounds for 2–4 year Python/Django backend roles. Next step is usually: solve → explain complexity → optimize → write production-quality Python.