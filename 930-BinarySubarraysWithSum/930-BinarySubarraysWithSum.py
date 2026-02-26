# Last updated: 2/25/2026, 11:29:54 PM
1"""
2UNDERSTAND
3- Given binary arr (contains only 0, 1) return the number of subarrays with a sum == goal
4- This is literally the same as subarray sum == k
5
6PLAN 
7- Hashmap to track previous prefix sums and their counts, at every step keep a running total, the number of prefix sums subtracted from our total that equal goal are number of subarrays
8"""
9from collections import defaultdict
10class Solution:
11    def _numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
12        if goal < 0: return 0
13        
14        res = 0
15        l = 0
16        total = 0
17
18        for r in range(len(nums)):
19            total += nums[r]
20
21            while total > goal:
22                total -= nums[l]
23                l += 1
24
25            res += r - l + 1
26
27        return res
28    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
29        return self._numSubarraysWithSum(nums, goal) - self._numSubarraysWithSum(nums, goal - 1)