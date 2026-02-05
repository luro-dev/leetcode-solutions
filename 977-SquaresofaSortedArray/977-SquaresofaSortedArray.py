# Last updated: 2/5/2026, 3:41:21 PM
1"""
2- Pattern: Two Pointers
3
4- Problem: Given an input list nums, sorted in ascending order, return an array of the squares of each number that is also sorted in ascending order.
5
6- Approach: Use a pointer at the beginning and one at the end, move them towards each other based on a check. We also want to initialize a list of size nums: As we iterate we check if abs(left) > abs(right) if it is we add it to the end of the list and decrement a pointer that points to the end of the result list to build the list rightmost greatest to leftmost smallest.
7- Do this until the pointers meet.
8
9"""
10
11class Solution:
12    def sortedSquares(self, nums: List[int]) -> List[int]:
13    
14        left = 0
15        right = len(nums) - 1
16        insert_idx = len(nums) - 1
17        res = [0] * len(nums)
18
19        while left <= right:
20            left_num = abs(nums[left])
21            right_num = abs(nums[right])
22
23            if left_num > right_num:
24                res[insert_idx] = left_num ** 2
25                left += 1
26            else:
27                res[insert_idx] = right_num ** 2
28                right -= 1 
29
30            insert_idx -= 1
31
32        return res
33
34        