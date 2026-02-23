# Last updated: 2/23/2026, 6:06:56 PM
1"""
2- So this has to be a counting problem with a sliding window. 
3- We have to go through the string and keep a map of seen characters, if at any point a new character reaches a count > 1 we must iterate from the left and delete as we go.
4
5"""
6from collections import defaultdict
7class Solution:
8    def lengthOfLongestSubstring(self, s: str) -> int:
9        seen = defaultdict(int)
10        max_sub = 0
11        left = 0
12
13        for right in range(len(s)):
14            seen[s[right]] += 1
15
16            while seen[s[right]] > 1:
17                seen[s[left]] -= 1
18                left += 1
19
20            max_sub = max(max_sub, right - left + 1)
21        
22        return max_sub
23