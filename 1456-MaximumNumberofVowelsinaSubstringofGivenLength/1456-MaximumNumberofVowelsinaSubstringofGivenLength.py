# Last updated: 2/11/2026, 2:13:18 PM
1"""
2- So here we have a sliding window problem with a fixed window size,
3- After creating our first window and calculating vowel count, we can remove leftmost by shifting index and recording if it was a vowel as well as moving foward one index
4
5- we need a most_vowels var and curr vowels
6- no need to change to lowercase, already done, k will be less than or equal to length of s
7"""
8class Solution:
9    def maxVowels(self, s: str, k: int) -> int:
10        vowels = set(['a', 'e', 'i', 'o', 'u'])
11        curr_vowels = 0
12
13        for i in range(0, k):
14            if s[i] in vowels:
15                curr_vowels += 1
16        
17        max_vowels = curr_vowels
18        
19        for i in range (k, len(s)):
20            if s[i] in vowels:
21                curr_vowels += 1
22            if s[i - k] in vowels:
23                curr_vowels -= 1
24            
25            max_vowels = max(curr_vowels, max_vowels)
26
27        return max_vowels
28
29