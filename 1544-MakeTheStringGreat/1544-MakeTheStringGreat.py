# Last updated: 3/19/2026, 6:16:02 PM
1class Solution:
2    def makeGood(self, s: str) -> str:
3        stack = []
4        print(ord('a'), ord('A'))
5        for c in s:
6            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
7                stack.pop()
8            else:
9                stack.append(c)
10        
11        return ''.join(stack)