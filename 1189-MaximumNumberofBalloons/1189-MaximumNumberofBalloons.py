# Last updated: 2/17/2026, 10:25:22 AM
1from collections import Counter
2
3"""
4UNDERSTAND
5- Given a string text, we want to return how many times we can make the word BALLOON using every character at most one time.
6
7PLAN
8- Count all the characters of the string text, and then mod the characters that require more than one, then return the minimum frequency since that character will be the bottleneck
9
10"""
11class Solution:
12    def maxNumberOfBalloons(self, text: str) -> int:
13        letter_counts = Counter(text)
14        min_freq = float('inf')
15        balloon_counter = Counter('balloon')
16
17        for letter, count in balloon_counter.items():
18            if letter not in letter_counts:
19                return 0
20
21            lett_freq = letter_counts[letter] // count
22            min_freq = min(min_freq, lett_freq)
23
24        return min_freq 
25