# Last updated: 3/11/2026, 10:35:27 AM
1from collections import defaultdict
2class Solution:
3    def twoSum(self, nums: List[int], target: int) -> List[int]:
4        seen = defaultdict(int)
5
6        for i in range(len(nums)):
7            looking_for = target - nums[i]
8
9            if looking_for in seen:
10                return [i, seen[looking_for]]
11            
12            seen[nums[i]] = i