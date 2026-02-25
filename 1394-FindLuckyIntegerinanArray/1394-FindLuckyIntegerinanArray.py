# Last updated: 2/25/2026, 6:37:26 PM
1"""
2UNDERSTAND
3- Given integer arr (pos ints) find the maximum lucky integer, a lucky int is a number that has a frequency == value
4- i.e 5 shows up 5 times in the arr
5
6PLAN
7- Count frequencies, maintain global max, every time a lucky int is found run a max func to see if > curr max lucky int
8"""
9from collections import Counter
10class Solution:
11    def findLucky(self, arr: List[int]) -> int:
12        freq_map = Counter(arr)
13        max_lucky = -1
14
15        for k, v in freq_map.items():
16            if k == v:
17                max_lucky = max(max_lucky, k)
18        
19        return max_lucky