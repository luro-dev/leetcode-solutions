# Last updated: 2/24/2026, 12:58:15 PM
1"""
2- Understand:
3We are given an array containing numbers (integers pos & neg)
4We want to return true if any value appears at least twice, else false if all distinct
5
6- Plan 
7Count frequences, if any freq > 1 return true else if none > 1 return false
8
9"""
10from collections import Counter
11class Solution:
12    def containsDuplicate(self, nums: List[int]) -> bool:
13        freq_map = Counter(nums)
14
15        for freq in freq_map.values():
16            if freq > 1:
17                return True
18        
19        return False