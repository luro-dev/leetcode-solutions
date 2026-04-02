# Last updated: 4/2/2026, 9:46:55 AM
1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        nums1_idx = { n:i for i, n in enumerate(nums1) }
4        res = [-1] * len(nums1)
5        stack = []
6
7        for i in range(len(nums2)):
8            curr_num = nums2[i]
9            if curr_num in nums1_idx:
10                for j in range(i+1, len(nums2)):
11                    if nums2[j] > curr_num:
12                        idx = nums1_idx[curr_num]
13                        res[idx] = nums2[j]
14                        break
15                 
16        return res