# Last updated: 2/25/2026, 7:26:04 PM
1"""
2- Given a string s, sort it in decreasing order based on the frequency of the characters
3- Bascially, count the characters, and then insert them based on their frequency, from highest frequency to lowest
4"""
5
6from collections import Counter
7from collections import defaultdict
8class Solution:
9    def frequencySort(self, s: str) -> str:
10        freq_map = Counter(s)
11        grouped_pairs = defaultdict(list)
12        max_freq = 0
13
14        for character, freq in freq_map.items():
15            grouped_pairs[freq].append(character)
16            max_freq = max(freq, max_freq)
17        
18        res = [""] * len(s)
19        insertion = 0
20        for i in range(max_freq, 0, -1):
21            for char in grouped_pairs[i]:
22                res.append(char * i)
23
24        return "".join(res)
25        
26        
27        