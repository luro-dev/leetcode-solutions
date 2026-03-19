# Last updated: 3/19/2026, 12:37:41 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        split_path = path.split("/")
4        stack = []
5
6        for c in split_path:
7            if c == "..":
8                if stack:
9                    stack.pop()
10            elif c != "" and c != ".":
11                stack.append(c)
12
13
14        return '/' + '/'.join(stack)
15