# Last updated: 2/11/2026, 12:52:16 PM
1"""
2- Two pointers problem
3- One to keep track of index to swap and one to scan the array for non-zero elements moving them to the front keeping their order
4
5"""
6
7class Solution:
8    def moveZeroes(self, nums: List[int]) -> None:
9        l = 0
10
11        for r in range(len(nums)):
12            if nums[r] != 0:
13                nums[l], nums[r] = nums[r], nums[l]
14                l += 1
15
16        return nums
17
18