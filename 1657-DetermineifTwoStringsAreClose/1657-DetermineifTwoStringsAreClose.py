# Last updated: 3/3/2026, 11:28:36 AM
1from collections import Counter
2class Solution:
3    def closeStrings(self, word1: str, word2: str) -> bool:
4        # Return true if word1 and word2 are close else false
5        # two words are close if we can complete two operations and attain one from the other as a result
6        # 1 -> swap any two existing characters
7        # 2 -> transform every occurence of one existing character into another existing character
8
9        # We can use the operations as many times necessary on either string
10
11        # edge case, if they have differing length its impossible
12        # we should count word1 and word2
13        # they will be close if we can obtain one from other so we can just do w/ 1
14
15        # test if the count is the same if it isnt return false
16        # count freq of chars
17
18        if len(word1) != len(word2):
19            return False
20        if set(word1) != set(word2):
21            return False
22
23        wc1_fs = Counter(Counter(word1).values())
24        wc2_fs = Counter(Counter(word2).values())
25        
26        if wc1_fs == wc2_fs:
27            return True
28        
29        return False
30        
31
32
33    
34
35
36
37
38
39        