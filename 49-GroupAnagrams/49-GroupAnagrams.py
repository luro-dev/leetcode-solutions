# Last updated: 2/18/2026, 9:32:37 AM
1from collections import defaultdict
2
3"""
4- Sort strings, if two strings are anagrams they will have the same sorted order
5- return dict values
6"""
7
8class Solution:
9    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
10
11        groups = defaultdict(list)
12
13        for s in strs:
14            key = "".join(sorted(s))
15            groups[key].append(s)
16        
17        return list(groups.values())