# Last updated: 2/17/2026, 10:08:28 AM
1from collections import Counter
2
3"""
4UNDERSTAND:
5- Given an array of integers  <= 0, return the LARGEST UNIQUE (only appears once) INTEGER
6
7PLAN:
8- Collect frequency of numbers and then iterate through the numbers checking if the count == 1, if it is store in max and do this as you iterate through.
9
10"""
11class Solution:
12    def largestUniqueNumber(self, nums: List[int]) -> int:
13        ans = float('-inf')
14        freqMap = Counter(nums)
15
16        for number, count in freqMap.items():
17            if count == 1:
18                ans = max(ans, number)
19        
20        return ans if ans != float('-inf') else -1