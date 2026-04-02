# Last updated: 4/2/2026, 11:22:53 AM
1"""
2- Maintain a monotonic decreasing stack, once we find the next greater element for the current one, any other elements we see that are not greater than the current one get added to the stack, once we find a greater we can pop all elements from the stack and set the current largest as the greater of all of those
3"""
4class Solution:
5    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
6        n1_idx = {n : i for i, n in enumerate(nums1) }
7        res = [-1] * len(nums1)
8        stack = []
9
10        for i in range(len(nums2)):
11            curr = nums2[i]
12            
13            while stack and curr > stack[-1]:
14                val = stack.pop()
15                idx = n1_idx[val]
16                res[idx] = curr
17            if curr in n1_idx:
18                stack.append(curr)
19        return res
20
21
22            
23
24                