# Last updated: 2/10/2026, 3:11:53 PM
1"""
2- Simple running sum problem, we can leverage the prefix sums technique to increment the sum of each index by the previous total sum.
3"""
4class Solution:
5    def runningSum(self, nums: List[int]) -> List[int]:
6        prefix = [nums[0]]
7
8        for i in range(1, len(nums)):
9            prefix.append(nums[i] + prefix[-1])
10
11        return prefix