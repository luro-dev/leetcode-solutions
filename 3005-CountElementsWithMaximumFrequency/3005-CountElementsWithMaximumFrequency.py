# Last updated: 2/25/2026, 6:33:29 PM
1"""
2UNDERSTAND
3- Given an array of positive integers that is not empty, return the number of elements with the highest seen frequency
4- Basically return the count of the elements with the highest seen frequency
5
6PLAN 
7- Counter for numbers and their freq, store max freq in variable
8- Iterate through the map and tally up the count of the each number with the max frequency
9"""
10from collections import Counter
11class Solution:
12    def maxFrequencyElements(self, nums: List[int]) -> int:
13        freq_map = Counter(nums)
14        max_freq = max(freq_map.values())
15        res = 0
16
17        for k,v in freq_map.items():
18            if v == max_freq:
19                res += v
20        
21        return res