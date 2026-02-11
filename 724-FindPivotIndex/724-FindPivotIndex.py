# Last updated: 2/11/2026, 6:27:34 PM
1"""
2- Clear preifx sum problem, we iterate through the indices of nums and check the sum of subarray to left and right and compare, if they are equal we return the index
3
4- Edge cases we have to watch out for, if there is no pivot return -1
5- watch out when i == 0, and when i == len(nums) - 1, we have to treat left sum and right sum as 0 respectively
6"""
7
8class Solution:
9    def pivotIndex(self, nums: List[int]) -> int:
10        prefix = [nums[0]]
11        for i in range(1, len(nums)):
12            prefix.append(prefix[-1] + nums[i])
13
14        for i in range(len(nums)):
15            left_sum = 0 if i == 0 else prefix[i - 1]
16            right_sum = 0 if i == len(nums) - 1 else prefix[-1] - prefix[i]
17
18            if right_sum == left_sum:
19                return i
20
21        return -1