# Last updated: 2/12/2026, 8:01:59 PM
1class Solution:
2    def countElements(self, arr: List[int]) -> int:
3        res = 0
4        ele = set(arr)
5
6        for num in arr:
7            if (num + 1) in ele:
8                res += 1
9
10        return res