# Last updated: 2/25/2026, 6:44:18 PM
1"""
2UNDERSTAND
3- Given an arr of pos and neg ints return true if all occurences of each number is unique, else if we see any number more than once return false
4
5PLAN
6- Count frequencies, then count the frequnecy of each freqency (bruh)
7"""
8from collections import Counter
9class Solution:
10    def uniqueOccurrences(self, arr: List[int]) -> bool:
11        freq_of_numbers = Counter(arr)
12        freq_of_freq = Counter(freq_of_numbers.values())
13
14        for k, v in freq_of_freq.items():
15            if v > 1:
16                return False
17
18        return True
19        