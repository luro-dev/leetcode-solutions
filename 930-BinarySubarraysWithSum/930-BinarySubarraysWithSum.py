# Last updated: 2/25/2026, 10:33:57 PM
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
11    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
12        res = 0
13        counts = defaultdict(int)
14        total = 0
15
16        for r in range(len(nums)):
17            counts[total] += 1
18            total += nums[r]
19
20            res += counts[total - goal]
21
22        return res
23