# Last updated: 3/19/2026, 11:49:24 AM
1class Solution:
2    def removeDuplicates(self, s: str) -> str:
3        stack = []
4
5        for c in s:
6            if stack and stack[-1] == c:
7                stack.pop()
8            else:
9                stack.append(c)
10        
11        return "".join(stack)