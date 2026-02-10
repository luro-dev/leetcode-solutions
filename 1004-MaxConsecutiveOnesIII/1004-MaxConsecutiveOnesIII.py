# Last updated: 2/9/2026, 7:42:20 PM
1"""
2- Problem is a sliding window problem, this one has a dynamic window size because the contraint metric is easily seen as the longest subarray with at most k zeroes since we can flip at most k zeroes so we can treat them as one.
3
4- We can use a while loop to scan for 0's once the constraint metric is reached, if the value is 0 we decrement the count of zeroes and keep shifting a left pointer to shrink the window,
5
6- After making the window valid again record the size which is calulated with the right index - left index + 1, and check it against the current max
7"""
8class Solution:
9    def longestOnes(self, nums: List[int], k: int) -> int:
10        countZeroes = 0
11        left = 0
12        maxLength = float('-inf')
13
14        for right in range(len(nums)):
15            if nums[right] == 0:
16                countZeroes += 1
17
18            while countZeroes > k:
19                if nums[left] == 0:
20                    countZeroes -= 1
21                left += 1
22            
23            maxLength = max(maxLength, right - left + 1)
24
25        return maxLength