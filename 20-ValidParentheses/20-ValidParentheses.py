# Last updated: 3/19/2026, 11:37:11 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        matching = {'(': ')', '{': '}', '[': ']'}
4        stack = []
5
6        for c in s:
7            if c in matching:
8                stack.append(c)
9            else:
10                if not stack:
11                    return False
12                
13                most_recent = stack.pop()
14
15                if matching[most_recent] != c:
16                    return False
17
18        return not stack