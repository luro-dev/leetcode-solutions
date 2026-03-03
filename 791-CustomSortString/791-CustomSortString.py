# Last updated: 3/3/2026, 11:11:16 AM
1"""
2U:
3- Given two strings order and s, permute (place) the characters of s so they match the order that order was sorted
4- Basically sort the characters of s by the order they appear in order. 
5
6
7"""
8from collections import Counter
9class Solution:
10    def customSortString(self, order: str, s: str) -> str:
11        count_map = Counter(s)
12        res = []
13
14        for char in order:
15            res.append(char * count_map[char])
16        
17        for char in s:
18            if char not in order:
19                res.append(char * count_map[char])
20                del count_map[char]
21                
22        
23        return "".join(res)
24
25            
26