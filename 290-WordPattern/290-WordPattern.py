# Last updated: 2/27/2026, 2:09:23 PM
1"""
2UNDERSTAND
3- Match a letter with a word pattern, check if it is consistent
4- Very similar to isomorphic except instead of char to char its char to string
5
6"""
7
8class Solution:
9    def wordPattern(self, pattern: str, s: str) -> bool:
10        mapLett = {}
11        mapWord = {}
12
13        if len(pattern) != len(s.split(" ")):
14            return False
15
16        for lett, word in zip(pattern, s.split(" ")):
17            
18            if lett in mapLett and mapLett[lett] != word or word in mapWord and mapWord[word] != lett:
19                return False
20
21            mapLett[lett] = word
22            mapWord[word] = lett
23
24        return True