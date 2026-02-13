# Last updated: 2/12/2026, 7:54:43 PM
1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        total_sum = sum(nums)
4
5        actual_sum = 0
6        for i in range(len(nums) + 1):
7            actual_sum += i
8        
9        return actual_sum - total_sum