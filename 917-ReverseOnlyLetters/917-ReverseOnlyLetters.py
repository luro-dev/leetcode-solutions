# Last updated: 2/11/2026, 12:41:55 PM
1class Solution:
2    def reverseOnlyLetters(self, s: str) -> str:
3        left = 0
4        right = len(s) - 1
5        ss = list(s)
6        while left < right:
7            while left < right and not ss[left].isalpha():
8                left += 1
9            while right > left and not ss[right].isalpha():
10                right -= 1
11            
12            ss[left], ss[right] = ss[right], ss[left]
13            left += 1
14            right -= 1
15
16        return "".join(ss)        