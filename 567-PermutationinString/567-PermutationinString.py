# Last updated: 2/26/2026, 11:33:27 AM
1"""
2UNDERSTAND
3- Given two strings s1 and s2, return ture if s2 contains a permuation of s1
4- Basically given s1 which will be a string chceck if it is contained in any permutation in s2
5
6PLAN 
7- Sliding window of fixed size (size of the permutation)
8- check if frequencies are equal if they are return true
9
10"""
11from collections import Counter
12class Solution:
13    def checkInclusion(self, s1: str, s2: str) -> bool:
14        c_s1 = Counter(s1)
15
16        for i in range(0, len(s2)):
17            if c_s1 == Counter(s2[i : i + len(s1)]):
18                return True
19
20        return False