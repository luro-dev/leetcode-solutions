# Last updated: 5/15/2026, 1:14:29 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        hi = len(nums) - 1
4        lo = 0
5
6
7        while lo <= hi:
8            mid = (hi + lo) // 2
9
10            if nums[mid] < nums[hi]:
11                hi = mid
12            elif nums[mid] > nums[hi]:
13                lo = mid + 1
14            else:
15                return nums[mid]