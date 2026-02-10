# Last updated: 2/9/2026, 7:58:04 PM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        num_zeroes = 0
4        left = 0
5        ans = float('-inf')
6
7        for right in range(len(nums)):
8            if nums[right] == 0:
9                num_zeroes += 1
10
11            while num_zeroes >= 1:
12                if nums[left] == 0:
13                    num_zeroes -= 1
14                left += 1
15            
16            ans = max(ans, right - left + 1)
17        
18        return ans
19        