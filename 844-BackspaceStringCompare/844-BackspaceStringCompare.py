# Last updated: 3/19/2026, 12:07:07 PM
1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3        def build(s):
4            stack = []
5
6            for c in s:
7                if c != '#':
8                    stack.append(c)
9                else:
10                    if stack:
11                        stack.pop()
12            
13            return "".join(stack)
14
15        return build(s) == build(t)