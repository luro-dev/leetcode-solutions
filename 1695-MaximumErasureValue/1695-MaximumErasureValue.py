# Last updated: 2/26/2026, 11:00:06 AM
1"""
2UNDERSTAND
3- Given an array of positive integers nums, erase a subarray containing unique elements
4- The score is equal to the sum of all elements of the erased subarrray
5- Return the maximum score 
6
7PLAN 
8- We can use a hashmap to keep track of the number of unique elements
9- Sliding window with a hashmap and prefix sums since we will be calculating the sum of valid windows
10"""
11from collections import defaultdict
12class Solution:
13    def maximumUniqueSubarray(self, nums: List[int]) -> int:
14        count = defaultdict(int)
15        total = 0
16        res = 0
17        l = 0
18
19        for r in range(len(nums)):
20            total += nums[r]
21            count[nums[r]] += 1
22
23            while count[nums[r]] > 1:
24                count[nums[l]] -= 1
25                total -= nums[l]
26                l += 1
27            
28            res = max(res, total)
29
30        return res
31
32
33