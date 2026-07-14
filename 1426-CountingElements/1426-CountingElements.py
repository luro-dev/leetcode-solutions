# Last updated: 7/14/2026, 5:49:26 PM
1from collections import Counter
2class Solution:
3    def countElements(self, arr: List[int]) -> int:
4        ele_count = set(arr)
5        valid_count = 0
6        
7        for ele in arr:
8            if ele + 1 in ele_count:
9                valid_count += 1
10        
11        return valid_count
12        
13        