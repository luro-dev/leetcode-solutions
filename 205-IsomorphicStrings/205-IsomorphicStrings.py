# Last updated: 2/27/2026, 11:26:34 AM
1"""
2UNDERSTAND
3- Given two strings determine if they are isomprphic (return true if so)
4- Isomorphic - all characters in s1 can be replaced to get t
5
6PLAN
7- Bascially we need to map characters to others,
8- Use a dict to map char s to char t, and a set to track mapped chars from t
9- Two cases return false - if the s char is not mapped yet, but the t is then its false, or if the s char is mapped but the t char is different than the one the current s char is mapped to
10
11"""
12class Solution:
13    def isIsomorphic(self, s: str, t: str) -> bool:
14        mapped = set()
15        s_to_t = {}
16
17        for i in range(len(s)):
18            if s[i] not in s_to_t:
19
20                if t[i] in mapped:
21                    return False
22                
23                s_to_t[s[i]] = t[i]
24                mapped.add(t[i])  
25            else:
26                if s_to_t[s[i]] != t[i]:
27                    return False
28
29        return True