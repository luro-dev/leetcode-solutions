# Last updated: 2/11/2026, 1:19:26 PM
1"""
2- Sliding window problem, with a dynamic window
3- Contraint metric:  subarray sum
4- Numeric restriction:  >= target
5
6- "best" subarray has shortest length
7- the target can be greater than the entire array sum, in that case return 0
8
9- keep left ptr, right ptr to advance until sum > target, fix window with while loop advancing left and removing val at left index, when the window is valid calculate the size and compare to current max min length
10"""
11class Solution:
12    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
13        global_min = float('inf')
14        cSum = 0
15        l = 0
16
17        for r in range(len(nums)):
18            cSum += nums[r]
19
20            while cSum >= target:
21                global_min = min(global_min, r - l + 1)
22                cSum -= nums[l]
23                l += 1
24        
25
26        return 0 if global_min == float('inf') else global_min
27
28