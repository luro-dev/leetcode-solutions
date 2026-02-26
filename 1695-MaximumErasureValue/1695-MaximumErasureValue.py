# Last updated: 2/26/2026, 11:00:54 AM
1"""
2UNDERSTAND
3- Given an array of positive integers nums, erase a subarray containing unique elements
4- The score is equal to the sum of all elements of the erased subarrray
5- Return the maximum score 
6
7PLAN 
8- We can use a hashmap to keep track of the number of unique elements
9- Sliding window with a hashmap and running sum since we will be calculating the sum of valid windows
10- When constraint is broken move left foward removing until valid again
11"""
12from collections import defaultdict
13class Solution:
14    def maximumUniqueSubarray(self, nums: List[int]) -> int:
15        count = defaultdict(int)
16        total = 0
17        res = 0
18        l = 0
19
20        for r in range(len(nums)):
21            total += nums[r]
22            count[nums[r]] += 1
23
24            while count[nums[r]] > 1:
25                count[nums[l]] -= 1
26                total -= nums[l]
27                l += 1
28            
29            res = max(res, total)
30
31        return res
32
33
34