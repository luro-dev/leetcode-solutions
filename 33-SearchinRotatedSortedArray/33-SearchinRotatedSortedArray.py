# Last updated: 5/15/2026, 2:32:16 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        inflection_point = self.find_inflection_point(nums)
4
5        left_search = self.binary_search(0, inflection_point, nums, target)
6        right_search = self.binary_search(inflection_point, len(nums) - 1, nums, target)
7
8        return left_search if left_search != -1 else right_search
9
10    def binary_search(self, start, end, arr, target):
11        while start <= end:
12            mid = (start + end) // 2
13
14            if arr[mid] == target:
15                return mid
16            elif arr[mid] > target:
17                end = mid - 1
18            else:
19                start = mid + 1
20      
21        return -1
22  
23    def find_inflection_point(self, nums):
24        hi = len(nums) - 1
25        lo = 0
26
27        while lo < hi:
28            mid = (hi + lo) // 2
29
30            if nums[mid] > nums[hi]:
31                lo = mid + 1
32            else:
33                hi = mid
34
35        return lo