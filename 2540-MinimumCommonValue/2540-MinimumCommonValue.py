# Last updated: 2/11/2026, 12:45:29 PM
1"""
2- Sorted arrays, return min int common to both, if no common return -1
3- Two pointers, we can use two pointers,
4- check the first element since sorted, if one element is greater than the other increment the smaller element to try and match, if either one is exhausted return -1 else return the first common element since the arrays are sorted smallest -> largest
5
6"""
7class Solution:
8    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
9        l = 0
10        r = 0
11
12        while l < len(nums1) and r < len(nums2):
13            if nums1[l] == nums2[r]:
14                return nums1[l]
15            elif nums1[l] > nums2[r]:
16                r += 1
17            else:
18                l += 1
19        
20        return -1
21
22        