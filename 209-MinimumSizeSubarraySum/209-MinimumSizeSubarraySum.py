# Last updated: 2/11/2026, 1:21:21 PM
1"""
2- Sliding window problem, with a dynamic window
3- Contraint metric:  subarray sum
4- Numeric restriction:  >= target
5
6- "best" subarray has shortest length
7- the target can be greater than the entire array sum, in that case return 0
8
9- this is similar to problems like subarray sum but with a trick, instead of having a specific end constraint we have a possibility where we need to remove various elements to be less than target, each of those removals shrinks the size of the subarray and we need to also consider their length, so we will have a while loop updating our min value
10
11"""
12class Solution:
13    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
14        global_min = float('inf')
15        cSum = 0
16        l = 0
17
18        for r in range(len(nums)):
19            cSum += nums[r]
20
21            while cSum >= target:
22                global_min = min(global_min, r - l + 1)
23                cSum -= nums[l]
24                l += 1
25        
26
27        return 0 if global_min == float('inf') else global_min
28
29