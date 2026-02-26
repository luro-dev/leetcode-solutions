# Last updated: 2/26/2026, 12:15:25 PM
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
12from collections import defaultdict
13class Solution:
14    def checkInclusion(self, s1: str, s2: str) -> bool:
15        count_s1 = Counter(s1)
16        count_s2 = defaultdict(int)
17
18        if len(s1) > len(s2):
19            return False
20            
21        for i in range(len(s1)):
22            count_s2[s2[i]] += 1
23
24        if count_s1 == count_s2:
25            return True
26
27        for r in range(len(s1), len(s2)):
28            count_s2[s2[r]] += 1
29            count_s2[s2[r - len(s1)]]-= 1
30
31            if count_s1[s2[r - len(s1)]] == 0:
32                del count_s2[s2[r - len(s1)]]
33
34            if count_s1 == count_s2:
35                return True
36                
37
38        return False