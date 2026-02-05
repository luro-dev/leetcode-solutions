# Last updated: 2/5/2026, 3:29:35 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        l = 0
4        r = len(s) - 1
5
6        while l < r:
7            s[l], s[r] = s[r], s[l]
8            l += 1
9            r -= 1 
10
11        return s       
12
13"""
14Pattern: Two Pointers
15Approach: Establish pointers at the front and end idx of input and swap position of characters at those indices.
16"""