# Last updated: 2/25/2026, 10:16:58 PM
1"""
2UNDERSTAND
3- Given a pos int arr, return number of good pairs
4- A good pair is one where (i, j) and nums[i] == nums[j] and i < j
5
6
7PLAN 
8- Count frequencies
9- we know if we have 4 1's we can make 4 * 4-1 / 2 (remove duplicates) different pairs
10
11"""
12from collections import Counter
13class Solution:
14    def numIdenticalPairs(self, nums: List[int]) -> int:
15        res = 0
16        count = Counter(nums)
17
18        for k, v in count.items():
19            res += v * (v - 1) // 2
20        
21        return res