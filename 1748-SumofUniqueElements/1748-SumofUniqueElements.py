# Last updated: 2/25/2026, 6:27:35 PM
1"""
2UNDERSTAND
3- Given an integer array nums, return the sum of all elements that appear exactly once
4
5PLAN
6- Just count frequencies in dictionary, then iterate through k,v pairs and increment a sum variable with the key that has a value (frequency) of 1
7
8"""
9from collections import Counter
10class Solution:
11    def sumOfUnique(self, nums: List[int]) -> int:
12        num_freq = Counter(nums)
13        total = 0
14
15        for k, v in num_freq.items():
16            if v == 1:
17                total += k
18        
19        return total