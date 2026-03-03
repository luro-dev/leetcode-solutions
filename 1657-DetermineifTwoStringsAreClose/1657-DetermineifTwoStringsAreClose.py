# Last updated: 3/3/2026, 11:30:43 AM
1from collections import Counter
2class Solution:
3    def closeStrings(self, word1: str, word2: str) -> bool:
4        if len(word1) != len(word2) or set(word1) != set(word2): return False
5
6        wc1_fs = Counter(Counter(word1).values())
7        wc2_fs = Counter(Counter(word2).values())
8        
9        if wc1_fs == wc2_fs:
10            return True
11        
12        return False